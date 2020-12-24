import requests


def get_random_image(subreddit: str) -> str:
    """
    Gets a random image from a given subreddit

    :param str subreddit: The subreddit to search.
    :return str: The image URL
    """
    out = requests.get(
        'https://www.reddit.com/r/{}/random.json'.format(subreddit),
        headers={'User-agent': 'douchebot'}
    )
    out.raise_for_status()
    body = out.json()
    data = body[0]['data']['children'][0]['data']
    if data.get('media'):
        if data['media'].get('type') == 'gfycat.com':
            return data['media']['oembed']['thumbnail_url']
    return data.get('url')
