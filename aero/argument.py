# -*- coding: utf-8 -*-
import textwrap

__author__ = 'nickl-'
from __version__ import __version__

from adapters import AVAILABLE_ADAPTERS
import os
import argparse
import re
import sys
import subprocess
from command import SearchCommand, InstallCommand, InfoCommand

AERO_PATH = os.path.dirname(os.path.realpath(__file__))


class ArgumentDelegate(argparse.ArgumentParser):
    pager = None

    class UsageFormatter(argparse.RawTextHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
        def _get_help_string(self, action):
            action.help = textwrap.fill(re.sub('\n| +', ' ', action.help), 54).replace('Choose one', 'Choose one')
            help = super(self.__class__, self)._get_help_string(action)
            return help.replace('(default: %(default)s)', '\n\ndefault: %(default)s\n\n')

        def _format_action_invocation(self, action):
            if not action.option_strings:
                return self._metavar_formatter(action, action.dest)(1)[0]
            args_string = self._format_args(action, action.dest.upper())
            if action.nargs > 1:
                args_string = "{}\n".format(args_string)
            return '{} {}'.format(', '.join(action.option_strings), args_string)

        def _fill_text(self, text, width, indent):
            return super(self.__class__, self)._fill_text(textwrap.dedent(text), width, indent)

    def __init__(self, prog='', version=''):

        with open(os.path.join(AERO_PATH, "assets", "descrip.ascii"), "r") as file:
            content = ''.join(file.readlines())
        with open(os.path.join(AERO_PATH, "assets", "epilog.ascii"), "r") as file:
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
                default_prefix + 'v', default_prefix * 2 + 'version',
                action='version', default=argparse.SUPPRESS,
                version=self.version,
                help="Show program's version number and exit",
            )

        self.add_argument(
            default_prefix + 'p', default_prefix * 2 + 'pager',
            help='''The pager to use for long paged displays. The default
            is based on the environment variable $PAGER, if it is
            not set, some common pagers like "less", "more", "most"
             and finally "cat" are tried, in this order.''',
            default=self.discover_pager(),
        )

        choices = list(type(x).__name__ for x in AVAILABLE_ADAPTERS) + ['Colour']

        self.add_argument(
            default_prefix + 'd', default_prefix * 2 + 'disable',
            action='append', dest='disabled',
            const='disabled',
            help='''Add the items you wish to disable to the list.
                Multiple disable arguments may be supplied.
                ''',
            default=[], choices=choices, nargs='?',
        )

        self.add_argument(
            default_prefix + 'i', default_prefix * 2 + 'invalidate-cache',
            action='store_true',
            dest='invalidate',
            help='''Clear the search cache and enquire anew from the
                package managers.''',
        )

        self.add_argument(
            default_prefix + 'c', default_prefix * 2 + 'completion',
            action=CompletionResponse,
            help='''Command outo completion is supported for both bash and zsh.
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

    def discover_pager(self, pager=None):
        if not ArgumentDelegate.pager:
            try:
                pagers = [os.environ['PAGER']]
            except KeyError:
                pagers = []
            pagers += ['less', 'more', 'most', 'cat']
            if pager is not None:
                pagers = [pager] + pagers
            for pager in pagers:
                p = subprocess.Popen(
                    ["type", pager],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE).communicate()[0]
                if 'not found' not in p:
                    r = re.match('^[^/]*([/\w]*)', p).groups()[0]
                    if r:
                        ArgumentDelegate.pager = r
                        break

        return ArgumentDelegate.pager

    def convert_arg_line_to_args(self, conf):
        for arg in conf.split(','):
            yield arg

    def add_package_commands(self, cmds):
        commargs = self.add_subparsers(
            metavar='command [mngr:] package',
            title="Command arguments", action=CommandParser,
            description='''
                The aero commands are based on the typical package manager
                commands followed by the package name to perform the task on.
                Use "aero cammand --help" to get further details for specific
                commands.''',
            help='''Optionally provide the specific manager to use prepended to
                the package name with a colon ":" or alternatively aero will
                execute the command against all enabled package managers.
                ##choose one of the following valid aero commands:##''',
        )
        procs = {}
        for k in cmds.keys():
            procs[k] = commargs.add_parser(k, help=cmds[k][0])
            procs[k].add_argument('package', help=cmds[k][1])

    def format_usage(self):
        return self.version + '\n\n' + super(self.__class__, self).format_usage()

    def format_help(self):
        with open(os.path.join(AERO_PATH,  "assets", "title.ascii"), "r") as file:
            content = ''.join(file.readlines()).replace('{{version}}', self.version)
            file.close()
        from random import choice
        aerotip = choice(('aero1', 'aero2', 'aero3', 'aero4', 'aero5', 'aero6', 'aero7', 'aero8'))
        with open(os.path.join(AERO_PATH, "assets/", aerotip + ".ascii"), "r") as file:
            aerotip = ''.join(file.readlines())
            file.close()
#        commhead = None
        with open(os.path.join(AERO_PATH, "assets", "command.ascii"), "r") as file:
            commhead = ''.join(file.readlines())
            file.close()

        content += super(self.__class__, self).format_help()\
            .replace('usage:', '\n')\
            .replace('r:] pack', 'r:]pack')\
            .replace('{{aerotip}}', aerotip)\
            .replace('Command arguments:', ''.join([commhead, '\n', 'Command arguments:']))
        content = re.sub(r'##(.+)\n\s*(.+)##', r'\n\n    \1 \2\n', content)
        return  content

    def _print_message(self, message, file=None):
        if message:
            if len(message.splitlines()) > 30:  # TODO find real screen height
                arg = self.prefix_chars[0] + 'p'
                args = [arg, self.prefix_chars[0] + arg + 'ager']
                pg = None
                for arg in args:
                    if arg in sys.argv and sys.argv.index(arg) + 1 <= len(sys.argv) - 1:
                        pg = sys.argv[sys.argv.index(arg) + 1]
                        ArgumentDelegate.pager = None
                        break
                pager = open('/tmp/aero.help.out', 'w')
                pager.write(message)
                pager.close()
                subprocess.Popen(self.discover_pager(pg) + ' /tmp/aero.help.out', shell=True).wait()
            else:
                if file is None:
                    file = sys.stderr
                file.write(message)


class CompletionResponse(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        completion_script = {
            'bash': """
_aero_completion()
{
    COMPREPLY=( $( COMP_WORDS="${COMP_WORDS[*]}" \\
                   COMP_CWORD=$COMP_CWORD \\
                   AERO_AUTO_COMPLETE=1 $1 ) )
}
complete -o default -F _aero_completion aero
""", 'zsh': """
function _aero_completion {
  local words cword
  read -Ac words
  read -cn cword
  reply=( $( COMP_WORDS="$words[*]" \\
             COMP_CWORD=$(( cword-1 )) \\
             AERO_AUTO_COMPLETE=1 $words[1] ) )
}
compctl -K _aero_completion aero
"""}
        print completion_script[values]
        parser.exit()


class CommandParser(argparse._SubParsersAction):
    def __call__(self, parser, data, values, option_string=None):
        super(self.__class__, self).__call__(parser, data, values, option_string)

        cmd = values[0]
        if ':' in values[1]:
            mngr = values[1].partition(':')
            pkg = mngr[2]
            mngr = mngr[0]
        else:
            mngr = None
            pkg = values[1]

        getattr(globals()[cmd.capitalize() + 'Command'](data), 'do')(pkg, data, mngr)
        print
