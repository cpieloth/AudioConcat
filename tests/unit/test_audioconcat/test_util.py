import unittest

from audioconcat.util import remove_special_characters


class TestRemoveSpecialCharacters(unittest.TestCase):

    def test_umlaute(self):
        input_str = 'foö baär'
        expected = 'fooe baaer'

        actual = remove_special_characters(input_str)
        self.assertEqual(expected, actual)
