from unittest import TestCase

from ..bible import random_bible_verse


class Test(TestCase):
    def test_random_bible_verse(self):
        verse = random_bible_verse()
        self.assertIsNotNone(verse)
