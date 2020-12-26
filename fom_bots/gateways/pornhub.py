from random import randint

import requests


def search_videos(search_string: str) -> str:
    res = requests.get(
        'http://www.pornhub.com/webmasters/search',
        params={"search": search_string}
    )
    res.raise_for_status()
    videos = res.json()['videos']
    video = videos[randint(0, len(videos) - 1)]
    return video['url']
