from unittest import TestCase

from .pornhub import search_videos


class Test(TestCase):
    def test_search_videos(self):
        res = search_videos("boob")
        self.assertIsNotNone(res)
