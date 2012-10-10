#!/usr/bin/env python
from __future__ import print_function

__version__ = '0.0.1'
import warnings
warnings.resetwarnings()
import os
from adapters import AVAILABLE_ADAPTERS
import argparse
import beaker
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

AERO_PATH=os.path.dirname(os.path.realpath(__file__)) + os.sep

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

class ArgumentDelegate(argparse.ArgumentParser):
    class UsageFormatter(argparse.RawTextHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
        def _get_help_string(self, action):
            help = super(self.__class__, self)._get_help_string(action)
            return help.replace('(default: %(default)s)', '\ndefault: %(default)s')

    def __init__(
                self,
                prog='',
                version='',
            ):

        with open(AERO_PATH+"assets/descrip.ascii","r") as file:
            content = ''.join(file.readlines())
        with open(AERO_PATH+"assets/epilog.ascii","r") as file:
            epilog = ''.join(file.readlines())
        super(self.__class__, self).__init__(
            description=content,

            formatter_class=self.UsageFormatter,
            epilog=epilog,
            fromfile_prefix_chars='@',
        )

        self.version = prog + ' ' + version
        if '-' in self.prefix_chars:
            default_prefix = '-'
        else:
            default_prefix = self.prefix_chars[0]

        if self.version:
            self.add_argument(
                default_prefix+'v', default_prefix*2+'version',
                action='version', default=argparse.SUPPRESS,
                version=self.version,
                help="show program's version number and exit",
            )

        choices = list(type(x).__name__ for x in AVAILABLE_ADAPTERS)+['Colour']

        self.add_argument(default_prefix+'d', default_prefix*2+'disable',
            action='append', dest='disabled',
            const='disabled', help='Add items to disable to the list',
            default=[], choices=choices, nargs='?',
        )

        self.add_argument(
            default_prefix+'i', default_prefix*2+'invalidate-cache',
            action='store_true',
            dest='invalidate',
            help="Clear the search cache",
        )


    def convert_arg_line_to_args(self, conf):
        for arg in conf.split(','):
            yield arg

    def add_package_commands(self, cmds):
        commargs = self.add_subparsers(metavar='command',
            title="Title addsub", help='Choose one of the following valid aero commands:',
            description="Some long and winding description", action=CommandParser,
        )
        procs = {}
        for k in cmds.keys():
            procs[k] = commargs.add_parser(k, help=cmds[k][0])
            procs[k].add_argument('package', help=cmds[k][1])

    def format_usage(self):
        return self.version + '\n\n' + super(self.__class__, self).format_usage()
#
    def format_help(self):
        with open(AERO_PATH+"assets/title.ascii","r") as file:
            content = ''.join(file.readlines()).replace('{{version}}', self.version)
        return  content + super(self.__class__, self).format_help().replace('usage:','\n').replace('}],','}],\n')


class CacheProvider():
    data = {}
    def seen(self, key, val=False):
        try:
            for k, v in key.items():
                self.data[k] = v
            return
        except AttributeError:
            pass

        if val or not isinstance(val,bool) and key not in self.data:
            self.data[key] = val

        try:
            return self.data[key]
        except KeyError:
            return False

    def invalidate(self, key, expires=None):
        if isinstance(expires, bool):
            del self.data[key]
        elif isinstance(key, bool):
            self.data = {}
        elif expires == None:
            return False # check if key is valid

class BeakerCacheProvider():
    cache = None
    def seen(self, key, val=False):
        try:
            for k, v in key.items():
                self.cache.put(k, v)
            return
        except AttributeError:
            pass

        if val or not isinstance(val,bool):
            try:
                res = self.cache.get(key)
                if res:
                    return res
            except KeyError:
                pass
            self.cache.put(key, val)

        try:
            return self.cache.get(key)
        except KeyError:
            return False

    def invalidate(self, key, expires=None):
        if isinstance(expires, bool):
            self.cache.remove_value(key)
        elif isinstance(key, bool):
            self.cache.clear()
        elif expires == None:
            return False # check if key is valid

class CacheProviderFactory():
    def whichProvider (self):
        if (beaker):
            return BeakerCacheProvider()
        else:
            return CacheProvider()


class CommandParser(argparse._SubParsersAction):
    cache = CacheProviderFactory().whichProvider()

    def __call__(self, parser, data, values, option_string=None):
        super(self.__class__, self).__call__(parser, data, values, option_string)

        if (data.invalidate): self.cache.invalidate(True)
        cmd = values[0]
        if ':' in values[1]:
            mngr = values[1].split(':',1)
            pkg = mngr.pop()
            mngr = mngr.pop()
        else:
            mngr = ''
            pkg = values[1]
        for case in switch(cmd):
            if case('install'):
                for adapter in AVAILABLE_ADAPTERS:
                    dptr = type(adapter).__name__
                    if dptr not in data.disabled:
                        if not mngr or mngr == dptr.lower():
                            print('Doing an aero %s of package: %r using %s ' % (cmd, pkg, type(adapter).__name__), end="")
                            getattr(adapter, cmd)(pkg)
                exit()
                break

        res = self.cache.seen(pkg)
        print('\nCommand Parser ns:%r val:%r opt:%r mngr:%s, pkg:%s cmd:%s\n' % (data, values, option_string, mngr, pkg, cmd))
        if data.invalidate or res == False:
            res = {}
            for adapter in AVAILABLE_ADAPTERS:
                dptr = type(adapter).__name__
                if dptr not in data.disabled:
                    if not mngr or mngr == dptr.lower():
                        print('Doing an aero %s of package: %r using %s ' % (cmd, pkg, type(adapter).__name__), end="")
                        aero = getattr(adapter, cmd)(pkg)
                        print('Found (%d) options' % (len(aero)))
                        res.update(aero)

        pager = ''
        if res:
            from subprocess import Popen
            import textwrap
            if (len(res) > 30): pager = '> /tmp/aero.out'
            Popen('printf "\n\n%50s %-50s\n" "PACKAGE NAME" "DESCRIPTION" '+pager, shell=True)
            if pager: pager = '>' + pager

        for k,v in sorted(self.cache.seen(pkg, res).items()):
            for wrap in textwrap.wrap(v, 50):
                Popen('printf "%50s %-50s\n" "'+k+'" "'+wrap+'" '+pager, shell=True)
                k = ''
        if pager:
            Popen('less /tmp/aero.out', shell=True).wait()

def main():
    cache_opts = {
        'cache.type': 'file',
        'cache.data_dir': '/tmp/cache/data',
        'cache.lock_dir': '/tmp/cache/lock'
    }

    cache = CacheManager(**parse_cache_config_options(cache_opts))
    BeakerCacheProvider.cache =  cache.get_cache('aero.cache', type='file', expire=604800)

    argp = ArgumentDelegate(
        prog='aero',
        version='v'+__version__,
    )
    argp.add_package_commands({
        'search': [
            'Do an aero search for a package',
            'The package name to aero search',
            ],
        'install': [
            'Do an aero install package',
            'The package name to aero install',
            ],
        }
    )

    args = argp.parse_args()

if __name__ == "__main__": main()
