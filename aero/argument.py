# -*- coding: utf-8 -*-
__author__ = 'nickl-'
from __version__ import __version__
from .adapters import AVAILABLE_ADAPTERS
from os import path
AERO_PATH = path.dirname(path.realpath(__file__))

from argparse import Namespace, ArgumentParser

class ArgumentDelegate(ArgumentParser):

    class ArgumentData(Namespace):

        choices = ['less', 'more', 'most', 'cat']
        _pager = None

        @property
        def pager(self):
            if not self._pager:
                self._pager = self.discover_pager()
            return self._pager

        @pager.setter
        def pager(self, val):
            self._pager = self.discover_pager([val])

        def discover_pager(self, pagers=[]):
            try:
                from os import environ
                pagers += [environ['PAGER']]
            except KeyError:
                pass
            pagers += self.choices
            from subprocess import Popen, PIPE
            for pager in pagers:
                p = Popen(
                    ['which', pager],
                    stdout=PIPE,
                    stderr=PIPE
                )
                if p.wait() == 0:
                    out = p.stdout.read().strip()
                    return out if pager != 'less' else out + ' -r'


    data = ArgumentData()

    from argparse import RawTextHelpFormatter, ArgumentDefaultsHelpFormatter

    class UsageFormatter(RawTextHelpFormatter, ArgumentDefaultsHelpFormatter):

        def _get_help_string(self, action):
            from re import sub
            from textwrap import fill
            action.help = fill(
                sub('\n| +', ' ', action.help), 54
            ).replace('Choose one', 'Choose one')
            help = super(self.__class__, self)._get_help_string(action)
            return help.replace(
                '(default: %(default)s)',
                '\n\ndefault: %(default)s\n\n'
            )

        def _format_action_invocation(self, action):
            if not action.option_strings:
                return self._metavar_formatter(action, action.dest)(1)[0]
            args_string = self._format_args(action, action.dest.upper())
            if action.nargs > 1:
                args_string = "{}\n".format(args_string)
            return '{} {}'.format(', '.join(action.option_strings), args_string)

        def _fill_text(self, text, width, indent):
            from textwrap import dedent
            return super(self.__class__, self)._fill_text(
                dedent(text), width, indent
            )

    def parse_args(self, args=None, namespace=None):
        '''
        pass the data collection so that we may also
        know what has been parsed.
        '''
        super(self.__class__, self).parse_args(args, self.data)

    def __init__(self, **kwargs):

        import codecs
        content = codecs.open(
            path.join(AERO_PATH, 'assets', 'descrip.ascii'),
            mode='r', 
            encoding='utf'
        ).read()
        epilog = codecs.open(
            path.join(AERO_PATH, 'assets', 'epilog.ascii'),
            mode='r', 
            encoding='utf'
        ).read()

        super(self.__class__, self).__init__(
            description=content,
            formatter_class=self.UsageFormatter,
            epilog=epilog,
            fromfile_prefix_chars='@',
        )

        # if there is no version then this instance is a subparser
        if '-' in self.prefix_chars:
            default_prefix = '-'
        else:
            default_prefix = self.prefix_chars[0]

        if kwargs.has_key('version'):
            self.version = kwargs['prog'] + ' ' + kwargs['version']

        if self.version:
            from argparse import SUPPRESS
            self.add_argument(
                default_prefix + 'v', default_prefix * 2 + 'version',
                action='version', default=argparse.SUPPRESS,
                version=self.version,
                help="Show program's version number and exit",
            )

        from argcomplete.completers import ChoicesCompleter
        self.add_argument(
            default_prefix + 'p', default_prefix * 2 + 'pager',
            help='''The pager to use for long paged displays. The default
            is based on the environment variable $PAGER, if it is
            not set, some common pagers like "less", "more", "most"
             and finally "cat" are tried, in this order.''',
            default=self.discover_pager(),
        ).completer=ChoicesCompleter(self.data.choices)

        self.add_argument(
            default_prefix + 'd', default_prefix * 2 + 'disable',
            action='append', dest='disabled',
            const='disabled',
            help='''Add the items you wish to disable to the list.
                Multiple disable arguments may be supplied.
                ''',
        )

        self.add_argument(
            default_prefix + 'i', default_prefix * 2 + 'invalidate-cache',
            action='store_true',
            dest='invalidate',
            help='''Clear the search cache and enquire anew from the
                package managers.''',
        )

        self.add_argument(
            default_prefix + '--', default_prefix * 2 + 'pass-through',
            dest='passthru',
            help='''Passthru arguments to be added as arguments to the
                package manager's command execution. Enclose the arguments
                in quotes to distinguish them from others.''',
        )

        self.add_argument(
            default_prefix + 'c', default_prefix * 2 + 'completion',
            action=CompletionResponse,
            help='''Command auto completion is supported for both bash and zsh.
                The result from the completion option can be appended to your
                .profile or simply using eval.
                ex.
                `       aero --completion zsh >> ~/.profile`
                Remember to source the changes.
                To use eval you might try something like:
                ex.
                `       eval "$(aero --completion bash)"`
                ''',
            choices=['bash', 'zsh']
        )



    def convert_arg_line_to_args(self, conf):
        for arg in conf.split(','):
            yield arg

    def add_package_commands(self, cmds):
        commargs = self.add_subparsers(
            metavar='command [mngr:] package',
            title="Command arguments", action=CommandParser,
            description='''
                The aero commands are based on the typical package manager
                commands followed by the package name(s) to perform the task on.
                At least one command is required but several packages can be
                processed simultaneously.
                Use "aero command --help" to get further details for specific
                commands.''',
            help='''Optionally provide the specific manager to use prepended to
                the package name(s) with a colon ":" or alternatively aero will
                execute the command against all enabled package managers.
                ##choose one of the following valid aero commands:##''',
        )
        procs = {}
        for k in cmds.keys():
            procs[k] = commargs.add_parser(k, help=cmds[k][0])
            procs[k].add_argument('packages', help=cmds[k][1], nargs='+')

    def format_usage(self):
        return self.version + '\n\n' + super(self.__class__, self).format_usage()

    def format_help(self):
        import codecs
        content = codecs.open(
            path.join(AERO_PATH,  'assets', 'title.ascii'),
            mode='r', 
            encoding='utf'
        ).read().replace('{{version}}', self.version)

        aerotip = choice(('aero1', 'aero2', 'aero3', 'aero4', 'aero5', 'aero6', 'aero7', 'aero8'))
        aerotip = codecs.open(
            path.join(AERO_PATH, 'assets/', aerotip + '.ascii'),
            mode='r',
            encoding='utf'
        ).read()

        commhead = codecs.open(
            path.join(AERO_PATH, 'assets', 'command.ascii'),
            mode='r',
            encoding='utf'
        ).read()

        content += super(self.__class__, self).format_help()\
            .replace('usage:', '\n')\
            .replace('r:] pack', 'r:]pack')\
            .replace('{{aerotip}}', aerotip)\
            .replace('Command arguments:', ''.join([commhead, '\n', 'Command arguments:']))
        from re import sub
        return sub(r'##(.+)\n\s*(.+)##', r'\n\n    \1 \2\n', content)

    def _print_message(self, message, file=None):
        if message:
            from pygments import highlight
            from pygments.lexers import guess_lexer
            from pygments.formatters import Terminal256Formatter
            message = highlight(message, guess_lexer(message), Terminal256Formatter())
            from commands import getTerminalSize
            height = getTerminalSize()[1]
            if len(message.splitlines()) > height:
                from subprocess import Popen, PIPE
                Popen(
                    self.data.pager, shell=True, stdin=PIPE
                ).communicate(input=message.encode('utf'))
            else:
                print message

from argparse import _SubParsersAction

class CommandParser(_SubParsersAction):

    def __call__(self, parser, data, values, option_string=None):
        super(self.__class__, self).__call__(parser, data, values, option_string)
        from importlib import import_module
        getattr(
            import_module('aero.commands.' + values[0]),
            values[0].capitalize() + 'Command'
        )(data).execute()
