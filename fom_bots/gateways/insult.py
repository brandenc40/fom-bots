import requests

INSULT_BASE_URL = 'https://go-insult-generator.herokuapp.com/'


def get_insult(endpoint):
    r = requests.get(INSULT_BASE_URL + endpoint)
    r.raise_for_status()
    results = r.json()
    if results['status'] == 'SUCCESS':
        return results['message']
    else:
        raise Exception(results['message'])
