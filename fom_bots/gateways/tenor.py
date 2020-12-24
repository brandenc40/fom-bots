import os

import requests


def search_gif(query: str) -> str:
    """
    Returns the img url of a top 4 result from tenor

    :param str query: A query string to search for
    :return str: The gif image url
    """
    params = {
        'key': os.environ.get('TENOR_API'),
        'q': query,
        'locale': 'en_US',
        'contentfilter': 'off',
        'media_filter': 'basic',
        'limit': 1,
        'pos': 0
    }
    out = requests.get("https://api.tenor.com/v1/search", params=params)
    if out.status_code == 200:
        out = out.json()
        if out['results']:
            url = out['results'][0]['media'][0]['gif']['url']
            return url
