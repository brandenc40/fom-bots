import requests


def get_insult():
    res = requests.get('http://pir.monkeyness.com/api/insult')
    res.raise_for_status()
    return res.text


def translate(text: str):
    res = requests.get("http://pirate.monkeyness.com/cgi-bin/translator.pl", params={"english": text})
    res.raise_for_status()
    return res.text
