import re
from random import choice

from groupme_bot import Context, ImageAttachment

from gateways import pornhub, reddit
from utils.error_decorator import handle_exceptions


@handle_exceptions
def porn(ctx: Context):
    res = re.search(r'^\\porn([a-zA-Z0-9 -_]+)', ctx.callback.text.lower())
    if res:
        query_string = res.group(1).strip()
    else:
        query_string = choice(['tits', 'ass', 'sexy'])
    url = pornhub.search_videos(query_string)
    if url:
        ctx.bot.post_message(url)
    else:
        ctx.bot.post_message(f"Nothing found for {query_string} you fucking pervert")


@handle_exceptions
def nsfw(ctx: Context):
    url = reddit.get_random_image('nsfw')
    try:
        gm_url = ctx.bot.image_url_to_groupme_image_url(url)
        ctx.bot.post_message("", [ImageAttachment(image_url=gm_url)])
    except Exception:
        ctx.bot.post_message(url)
