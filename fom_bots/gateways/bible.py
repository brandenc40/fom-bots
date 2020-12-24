from random import choice, randint

import requests
from bs4 import BeautifulSoup

from config import logger
from constants.bible_verses import BAD_VERSES


def random_bible_verse():
    if randint(1, 20) >= 10:
        try:
            return _random_bible_verse()
        except Exception as e:
            logger.error('error fetching bible verse from web page')
            logger.error(e)
            return _random_bad_bible_verse()
    else:
        return _random_bad_bible_verse()


def _random_bible_verse() -> str:
    r = requests.get('https://dailyverses.net/random-bible-verse')
    soup = BeautifulSoup(r.text, 'lxml')
    verse_div = soup.findAll("div", {"class": "bibleVerse"})[0]
    out = ''
    chapter = ''
    for content in verse_div.contents:
        if str(content) == '<br/>':
            out += ' '
        elif str(content).startswith('<div class="bibleChapter">'):
            chapter = content.findAll("div", {"class": "reference"})[0].text
        elif str(content).startswith('<'):
            continue
        else:
            out += content
    return out + ' - ' + chapter


def _random_bad_bible_verse():
    return choice(BAD_VERSES)
