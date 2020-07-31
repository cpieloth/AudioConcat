"""Entry point for package."""


import argparse as ag
import sys

import audioconcat.sub_commands


def main(argv=None):
    """
    CLI of AudioConcat.

    :return: 0 on success.
    """
    if not argv:
        argv = sys.argv

    # Parse arguments
    parser = ag.ArgumentParser(prog=argv[0])
    parser.add_argument('--version', action='version', version='%(prog)s ' + audioconcat.__version__)

    subparser = parser.add_subparsers(title='Commands', description='Valid Audio Concat commands.')
    audioconcat.sub_commands.ConcatCmd.init_subparser(subparser)

    args = parser.parse_args(argv[1:])
    try:
        # Check if a sub-command is given, otherwise print help.
        getattr(args, 'func')
    except AttributeError:
        parser.print_help()
        return 2

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
