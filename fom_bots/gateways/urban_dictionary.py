import requests
from bs4 import BeautifulSoup

from random import randint


def get_urban_dict(word: str = None) -> str:
    error_msg = None
    try:
        if word:
            params = {'term': word}
            endpoint = 'https://www.urbandictionary.com/define.php'
            error_msg = "Can't find anything for that one"
        else:
            params = {'page': randint(2, 10000)}
            endpoint = 'https://www.urbandictionary.com/random.php'
            error_msg = "It didn't fucking work Branden"
        r = requests.get(endpoint, params=params)
        soup = BeautifulSoup(r.content, "lxml")
        panel = soup.findAll("div", {"class": "def-panel"})[0]
        word = str(panel.findAll("a", {"class": "word"})[0].text.title())
        meaning = str(panel.findAll("div", {"class": "meaning"})[0].text)
        example = str(panel.findAll("div", {"class": "example"})[0].text)
        output = ''
        output += word
        output += '\n\nDefinition:\n'
        output += meaning
        if example:
            output += '\n\nHow to use it:\n'
            output += example
        output = output.replace('\r ', '\n\n').replace('\r', '\n')
        return output if output else error_msg
    except Exception:
        return error_msg
