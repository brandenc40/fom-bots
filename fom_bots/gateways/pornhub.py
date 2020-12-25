from random import randint

import requests
from bs4 import BeautifulSoup

PORNHUB_BASE_URL = 'http://www.pornhub.com/video/search'
PORNHUB_HEADERS = {"Content-Type": "text/html; charset=UTF-8"}


def search_videos(search_string: str) -> str:
    payload = {"search": "", "page": 1}
    keywords = search_string.split()
    for item in keywords:
        if (item == "professional") or (item == "pro"):
            payload["p"] = "professional"
        elif (item == "homemade") or (item == "home"):
            payload["p"] = "homemade"
        else:
            payload["search"] += (item + " ")

    r = requests.get(PORNHUB_BASE_URL, params=payload, headers=PORNHUB_HEADERS)
    b = BeautifulSoup(r.text, "lxml")
    videos = b.find_all("div", {"class": "phimage"})
    video = videos[randint(0, len(videos) - 1)]
    return 'http://www.pornhub.com' + video.find("a", href=True).attrs["href"]
