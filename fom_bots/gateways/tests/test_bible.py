from unittest import TestCase

from ..bible import _random_bible_verse


class Test(TestCase):
    def test_random_bible_verse(self):
        verse = _random_bible_verse()
        self.assertIsNotNone(verse)
        self.assertIsInstance(verse, str)
