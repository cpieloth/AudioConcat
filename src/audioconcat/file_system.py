"""
Basic file system functions.
"""

import logging
import pathlib

import audioconcat.util

logger = logging.getLogger(__name__)


def get_leaf_files(folder, whitelist=None):
    """
    Generator to retrieve a list of files per folder.

    :param folder: Folder to start recursive search.
    :param whitelist: Whitelist of file extensions to include.
    :return: A list of all files matching the whitelist in one folder.
    """
    if whitelist is None:
        whitelist = ['.mp3', '.wma']

    path = pathlib.Path(folder)
    files = []

    for path in path.iterdir():
        if path.is_dir():
            for sub_files in get_leaf_files(path):
                yield sub_files
        if path.is_file():
            if path.suffix in whitelist:
                files.append(path)
            else:
                logger.debug('File does not match whitelist: %s', path)
    if files:
        yield files


def check_and_get_directory(files):
    """
    Check if all provided files have the same directory and return it.

    :param files: A list of files to check and get directory from.
    :return: Base directory of the files.
    :raise: RuntimeException if files does not have same base directory.
    """
    if not files:
        raise ValueError('Files must not be empty!')

    head, *tail = files

    if not tail:
        return head.parent

    tail_parent = check_and_get_directory(tail)
    if head.parent == tail_parent:
        return head.parent

    raise RuntimeError(f'Files do not have the same directory: {head.parent} != {tail_parent}')


class FolderFiles:
    """
    Container class for files of one folder.
    """

    def __init__(self, files):
        self.files = files
        self.dir = check_and_get_directory(files)

    @property
    def name(self):
        return audioconcat.util.remove_special_characters(str(self.dir.name))

    @property
    def extensions(self):
        extensions = set()
        for file in self.files:
            extensions.add(file.suffix)
        return extensions

    def __str__(self):
        return (f'{self.__class__.__name__}: name={self.name}, '
                f'files={len(self.files)}, extensions={len(self.extensions)}, dir={self.dir}')
