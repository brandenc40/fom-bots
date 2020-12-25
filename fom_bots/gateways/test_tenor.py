from unittest import TestCase

from .tenor import search_gif


class Test(TestCase):
    def test_search_gif(self):
        gif_url = search_gif("dwight")
        self.assertIsNotNone(gif_url)
        self.assertRegexpMatches(
            gif_url, r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
