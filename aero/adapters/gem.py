# -*- coding: utf-8 -*-
__author__ = 'nickl-'
__all__ = ('Gem', )



from .base import BaseAdapter
from aero.__version__ import __version__, enc


class Gem(BaseAdapter):
    """
    Ruby gems adapter.
    """
    def search(self, query):
        response = self.command('search -qbd', query)[0].decode(*enc)
        from re import match
        lst = {}
        desc = False
        blank = False
        for line in [l for l in response.splitlines() if not match('\*\*\*',l)]:
            line = line.decode('utf')
            if not desc and match('(.*)\((.*)\)', line):
                key, val = match('(.*)\((.*)\)', line).groups()
                lst[self.package_name(key)] = 'Version: ' + val + '\n'
                desc = True
            elif desc and not blank and not line:
                blank = True
            elif desc and 'Homepage:' in line:
                lst[self.package_name(key)] += line.replace('Homepage: ', '').strip() + '\n'
            elif desc and blank and line:
                lst[self.package_name(key)] += line.strip() + ' '
            elif desc and blank and not line:
                desc = False
                blank = False
        return lst

    def install(self, query):
        self.shell('install', query).wait()
        return {}

    def info(self, query):

        import yaml

        class Timestamp(yaml.YAMLObject, dict):

            yaml_tag = '!timestamp'

            def __setstate__(self, state):
                self['at'] = state['at'][:state['at'].index(' ')]

        class Version(yaml.YAMLObject, dict):

            yaml_tag = '!ruby/object:Gem::Version'

            def __setstate__(self, state):
                self['version'] = state['version']


        class Requirement(yaml.YAMLObject, dict):

            yaml_tag = '!ruby/object:Gem::Requirement'

            def __setstate__(self, state):
                r = state['requirements'].pop()
                self['requirement'] = '{} {}'.format(r.pop(0), r.pop(0)['version'])


        class Dependency(yaml.YAMLObject, dict):

            yaml_tag = '!ruby/object:Gem::Dependency'

            def __setstate__(self, state):
                for require in [r for r in state.keys() if 'require' in r]:
                    try:
                        self['requirement'] = state[require]['requirement']
                        break
                    except KeyError:
                        continue
                self['name'] = state['name']
                self['type'] = state['type']


        class GemSpec(yaml.YAMLObject, dict):

            yaml_tag = '!ruby/object:Gem::Specification'

            def __setstate__(self, state):
                for k, v in [st for st in state.items() if st[1]]:
                    if isinstance(v, list):
                        if k == 'dependencies':
                            s = []
                            mx = 0
                            for dep in v:
                                mx = max(len(dep['name']), mx)
                                s.append((dep['name'], dep['type'], dep['requirement']))
                            mx += 1
                            s = '\n'.join(['{:{}}{:12} {:12}'.format(t[0], mx, t[1], t[2]) for t in s])
                            v = s
                        else:
                            v = ', '.join(v)
                    if isinstance(v, Timestamp):
                        v = v['at']
                    if isinstance(v, Version):
                        v = v['version']
                    if isinstance(v, Requirement):
                        v = v['requirement']
                    if not isinstance(v, str):
                        v = str(v)
                    self.update([(k, v)])

        response = self.command('specification -qb --yaml', query)[0].decode(*enc)
        if 'ERROR:' in response:
            return ['Aboted: {}\n'.format(response)]
        from re import sub
        result = yaml.load(sub(r'!binary', r'!!binary', response))
        try:
            return sorted(result.items())
        except AttributeError:
            return ['Aborted: No info available for a gem called: {}\n'.format(query)]
