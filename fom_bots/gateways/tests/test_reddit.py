from unittest import TestCase

from ..reddit import get_random_image


class Test(TestCase):
    def test_get_random_image(self):
        img_url = get_random_image("nsfw")
        self.assertIsNotNone(img_url)
        self.assertRegex(
            img_url, r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
