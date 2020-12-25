from unittest import TestCase

from .urban_dictionary import get_urban_dict


class Test(TestCase):
    def test_get_urban_dict(self):
        res = get_urban_dict("Tyler")
        self.assertIsNotNone(res)
        self.assertNotEqual(res, "Can't find anything for that one")

        res = get_urban_dict()
        self.assertIsNotNone(res)
        self.assertNotEqual(res, "It didn't fucking work Branden")
