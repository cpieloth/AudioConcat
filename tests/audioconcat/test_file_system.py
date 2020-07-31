import pathlib
import unittest

from audioconcat.file_system import check_and_get_directory
from audioconcat.file_system import get_leaf_files


class TestCheckAndGetDirectory(unittest.TestCase):

    def test_single_path(self):
        expected = pathlib.Path('foo/')
        files = [pathlib.Path('foo/bar')]

        actual = check_and_get_directory(files)
        self.assertEqual(expected, actual)

    def test_multi_path(self):
        expected = pathlib.Path('foo/')
        files = [pathlib.Path('foo/bar'), pathlib.Path('foo/baz'), pathlib.Path('foo/foo')]

        actual = check_and_get_directory(files)
        self.assertEqual(expected, actual)

    def test_exception(self):
        files = [pathlib.Path('foo/bar'), pathlib.Path('bar/baz'), pathlib.Path('foo/foo')]
        self.assertRaises(RuntimeError, check_and_get_directory, files)


class TestGetLeafFiles(unittest.TestCase):

    def test_non_empty(self):
        tests_dir = pathlib.Path(__file__).parent.parent
        folders_count = 0

        for files in get_leaf_files(tests_dir, whitelist=['.py']):
            self.assertGreater(len(files), 0)
            folders_count += 1

        self.assertGreater(folders_count, 0)

    def test_empty(self):
        tests_dir = pathlib.Path(__file__).parent.parent

        for _ in get_leaf_files(tests_dir, whitelist=['.foo']):
            self.fail('Files found, but expected none.')
