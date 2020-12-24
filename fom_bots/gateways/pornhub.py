from typing import List

import requests

API_URL = "http://www.pornhub.com/webmasters"
SEARCH_URL = API_URL + '/search'


def search_videos(query: str) -> List[dict]:
    response = requests.get(
        SEARCH_URL,
        params={'search': query, 'thumbnails': 'all'}
    )
    response.raise_for_status()
    return response.json()


def get_top_video_url(query: str) -> str:
    videos = search_videos(query)
    if videos:
        return videos[0].get('url')
