import re

from groupme_bot import Context

from constants import regex
from gateways import tenor
from utils.error_decorator import handle_exceptions


@handle_exceptions
def search_gif(ctx: Context):
    sr = re.search(regex.GIF + r'(.+)', ctx.callback.text)
    if sr:
        q_str = sr.group(1).strip()
        if q_str:
            gif_url = tenor.search_gif(ctx.callback.text)
            ctx.bot.post_message(gif_url)
            return
    ctx.bot.post_message("you didn't search anything... dumbass")
