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

#        self.UsageFormatter.outer = self;
#        self.ArgumentParser.outer = self
#        self.parser = self.ArgumentParser(

        #            prog=prog,
        #        formatter_class=argparse.RawDescriptionHelpFormatter,
        #        formatter_class=argparse.RawTextHelpFormatter,
        #        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
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


#            search = commargs.add_parser('search', help='Do an aero search for a package')
#            search.add_argument('package', help='The package name to aero search') #, action=FooAction)
#            install = commargs.add_parser('install', help='Do an aero install package')
#            install.add_argument('package', help='The package name to aero install') #, action=FooAction)

#    commargs = argp.add_subparsers(metavar='command package', title="Title addsub", help='Choose one of the following valid aero commands:', description="Some long and winding description", action=CommandParser)
#    search = commargs.add_parser('search', help='Do an aero search for a package')
#    search.add_argument('package', help='The package name to aero search') #, action=FooAction)
#    install = commargs.add_parser('install', help='Do an aero install package')
#    install.add_argument('package', help='The package name to aero install') #, action=FooAction)

#        if self.version:
#            self.add_argument(
#                self.parser.default_prefix+'v', self.parser.default_prefix*2+'version',
#                action='version', default=argparse.SUPPRESS,
#                version=self.version,
#                help=self.parser._("show program's version number and exit"))

#        self.add_argument("-v", "--version", action='version', version="aero x v0.0.1")
#        self.add_argument('search', help='search for a package')
#        self.add_argument("-s", dest='ip3octets', action='store', help='Enter the first, three,  octets of, the \nclass C,network to scan for live hosts', required=True)
#        self.add_argument("-p", dest='ip', action='store', help='conduct portscan of specified host', required=True)

#    def add_argument(self, *args, **kwargs):
#        return self.parser.add_argument(*args, **kwargs)

#    def parse_args(self):
#        return self.parser.parse_args()
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



    #    class ArgumentParser(argparse.ArgumentParser):
#        outer = None
#        def _get_formatter(self):
#            return self.formatter_class(prog=self.prog, outer=self)
#
    def format_usage(self):
        return self.version + '\n\n' + super(self.__class__, self).format_usage()
#
    def format_help(self):
        with open(AERO_PATH+"assets/title.ascii","r") as file:
            content = ''.join(file.readlines()).replace('{{version}}', self.version)
#        ver = textwrap.fill(self.version, 80, initial_indent=20, subsequent_indent=20)
            return  content + super(self.__class__, self).format_help().replace('usage:','\n').replace('}],','}],\n')


    class UsageFormatter(argparse.RawTextHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
#        def __init__(self, prog, indent_increment=2, max_help_position=24, width=None):
#            super(self.__class__, self).__init__(prog, indent_increment, max_help_position, width)
#            self._current_indent = 20
#            self._level = 10
#        def add_usage(self, usage, actions, groups, prefix=None):
#            print self.outer.version
            #        text = 'Version: %(version)s'  % dict(self._root_section.items) # dict(prog=self._prog version)
            #        self._add_item(self._format_text, [text])
#            super(self.__class__, self).add_usage(usage, actions, groups, prefix)

        def _get_help_string(self, action):
            help = super(self.__class__, self)._get_help_string(action)
            return help.replace('(default: %(default)s)', '\ndefault: %(default)s')

#        def _fill_text(self, text, width, indent):
#            return super(self.__class__, self)._fill_text(text, width, indent) #textwrap.dedent(text)




#class CustomUsageFormatter(argparse.RawTextHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
#
##    def add_usage(self, usage, actions, groups, prefix=None):
##        print self._current_section
##        #        text = 'Version: %(version)s'  % dict(self._root_section.items) # dict(prog=self._prog version)
##        #        self._add_item(self._format_text, [text])
##        super(self.__class__, self).add_usage(usage, actions, groups, prefix)
#
#    def _get_help_string(self, action):
#        help = super(self.__class__, self)._get_help_string(action)
#        return help.replace('(default: %(default)s)', '\ndefault: %(default)s')
#
#    def _fill_text(self, text, width, indent):
#        return super(self.__class__, self)._fill_text(textwrap.dedent(text), width, indent)
#


#def usage(x):
#    print x, " xxxThere would probably be some usage info here:"
#    pass


#    parser = ArgumentParser(
#        conflict_handler='resolve',
#        version="aero v0.0.1",
#        prog='aero',
##        formatter_class=argparse.RawDescriptionHelpFormatter,
##        formatter_class=argparse.RawTextHelpFormatter,
##        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
#        formatter_class=CustomUsageFormatter,
#        description=('''\
#             Please do not mess up this text!
#             --------------------------------
#                 I have indented it
#                 exactly the way
#                 I want it
#             '''),
#
#        epilog="What are you waiting for?",
#        fromfile_prefix_chars='@',
#    )
#    parser.add_argument("-v", "--version", action='version', version="aero x v0.0.1")
#    parser.add_argument("-s", dest='ip3octets', action='store', help='Enter the first, three,  octets of, the \nclass C,network to scan for live hosts', required=True)
#    parser.add_argument("-p", dest='ip', action='store', help='conduct portscan of specified host', required=True)

#    args = parser.parse_args()
#    class FooAction(argparse.Action):
#        def __call__(self, parser, namespace, values, option_string=None):
#            setattr(namespace, self.dest, values)
#            print '\n>>>ns:%r val:%r apt:%r\n' % (namespace, values, option_string)

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
#            setattr(namespace, self.dest, values)
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

#                setadapter.search(sys.argv[2])



def main():
    cache_opts = {
        'cache.type': 'file',
        'cache.data_dir': '/tmp/cache/data',
        'cache.lock_dir': '/tmp/cache/lock'
    }

    cache = CacheManager(**parse_cache_config_options(cache_opts))
    BeakerCacheProvider.cache =  cache.get_cache('aero.cache', type='file', expire=604800)
#    BeakerCacheProvider.cache.invalidate = cache.invalidate
    #metavar='cammand: available commands %(choices)'
#    argp = argparse.ArgumentParser()

#    argp.add_argument('invalidate', help='The package name to aero', action=FooAction)
#    argp.add_argument('command', help='One of the allowed aero commands', choices=['search', 'install'])#, nargs=2)
#    argp.add_argument('package', help='The package name to aero', action=FooAction)


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

    args = argp.parse_args()#'search'.split())

#    print args
#    print vars(args)
#    if 'command' in args: print args.command

if __name__ == "__main__": main()
#exit(0)

#print "============================\n\n=================================="
#argp = ArgumentParser(
#        version="aero v0.0.1",
#        description='A foo that bars',
#        epilog="And that's how you'd foo a bar",
#    )
#
## 'store_const',
##    dest='accumulate',
## dest='accumulate',
## action=usage,
#argp.add_argument(
#    dest='search',
#    action=usage,
#    nargs=2,
#    default="deffoult",
#    type=basestring,
#    choices=['search','-s'],
#    metavar='x')
#argp.add_argument("-s", dest='ip3octets', action='store', help='Enter the first three octets of the class C network to scan for live hosts')
##print arg.
##exit(0)
#args = argp.parse_args()
#print args # .accumulate(args.integers)
#
## TODO better command handling
#if len(sys.argv) == 1:
#    usage('')
#    exit(0)
#
#
#if sys.argv[1] == 'search':
#    if len(sys.argv) == 2:
#        print "Use search query"
#        exit(1)
#
#    for adapter in AVAILABLE_ADAPTERS:
#        print adapter
#        adapter.search(sys.argv[2])
#
