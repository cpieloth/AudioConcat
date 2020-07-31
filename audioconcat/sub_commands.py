"""Module for CLI command implementations."""

import abc
import pathlib

import audioconcat.concat


__author__ = 'christof.pieloth'


class SubCommand(abc.ABC):
    """
    Abstract base class for sub commands.

    A new sub command can be added by calling the init_subparser().
    """

    @classmethod
    @abc.abstractmethod
    def _name(cls):
        """
        Return name of the command.

        :return: Command name
        :rtype: str
        """
        raise NotImplementedError()

    @classmethod
    def _help(cls):
        """
        Return help description.

        :return: Help description
        :rtype: str
        """
        return cls.__doc__

    @classmethod
    @abc.abstractmethod
    def _add_arguments(cls, parser):
        """
        Initialize the argument parser and help for the specific sub-command.

        Must be implemented by a sub-command.

        :param parser: A parser.
        :type parser: argparse.ArgumentParser
        :return: void
        """
        raise NotImplementedError()

    @classmethod
    def init_subparser(cls, subparsers):
        """
        Initialize the argument parser and help for the specific sub-command.

        :param subparsers: A subparser.
        :type subparsers: argparse.ArgumentParser
        :return: void
        """
        parser = subparsers.add_parser(cls._name(), help=cls._help())
        cls._add_arguments(parser)
        parser.set_defaults(func=cls.execute)

    @classmethod
    @abc.abstractmethod
    def execute(cls, args):
        """
        Execute the command.

        Must be implemented by a sub-command.

        :param args: argparse arguments.
        :return: 0 on success.
        """
        raise NotImplementedError()


class ConcatCmd(SubCommand):
    """Retrieve and concat audio files per innermost folder."""

    @classmethod
    def _name(cls):
        return 'concat'

    @classmethod
    def _add_arguments(cls, parser):
        parser.add_argument('--input-dir', '-i', nargs='+', required=True, help='Directory to start recursive search.')
        parser.add_argument('--output-dir', '-o', required=True, help='Directory to store output files.')
        return parser

    @classmethod
    def execute(cls, args):
        output_dir = pathlib.Path(args.output_dir)

        for input_dir in args.input_dir:
            audioconcat.concat.retrieve_and_concat_audio_files(pathlib.Path(input_dir), output_dir)

        return 0
