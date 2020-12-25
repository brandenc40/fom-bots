from unittest import TestCase

from .insult import get_insult


class Test(TestCase):
    def test_get_insult(self):
        insult = get_insult('comeback')
        self.assertIsNotNone(insult)
        self.assertIsInstance(insult, str)
