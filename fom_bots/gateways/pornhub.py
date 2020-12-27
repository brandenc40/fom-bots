from random import randint

import requests


def search_videos(search_string: str) -> str:
    res = requests.get(
        'http://www.pornhub.com/webmasters/search',
        params={"search": search_string}
    )
    res.raise_for_status()
    json = res.json()
    videos = json.get('videos')
    if videos:
        video = videos[randint(0, min(len(videos) - 1, 5))]
        return video['url']
