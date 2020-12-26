from unittest import TestCase

from ..pornhub import search_videos


class Test(TestCase):
    def test_search_videos(self):
        res = search_videos("boob")
        self.assertIsNotNone(res)
        self.assertRegex(
            res, r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
