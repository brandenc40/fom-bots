import requests


def get_random_image(subreddit: str) -> str:
    """
    Gets a random image from a given subreddit

    :param str subreddit: The subreddit to search.
    :return str: The image URL
    """
    res = requests.get(
        f'https://www.reddit.com/r/{subreddit}/random.json',
        headers={'User-agent': 'douchebot'}
    )
    res.raise_for_status()
    body = res.json()
    data = body[0]['data']['children'][0]['data']
    if data.get('media'):
        if data['media'].get('type') == 'gfycat.com':
            return data['media']['oembed']['thumbnail_url']
    return data.get('url')
