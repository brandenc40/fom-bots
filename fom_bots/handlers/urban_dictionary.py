import re

from groupme_bot import Context

from constants import regex
from gateways import urban_dictionary
from utils.error_decorator import handle_exceptions


@handle_exceptions
def urban_dictionary_search(ctx: Context):
    sr = re.search(regex.URBAN + r'(.+)', ctx.callback.text)
    if sr:
        q_str = sr.group(1).strip()
        if q_str:
            msg = urban_dictionary.get_urban_dict(q_str)
            ctx.bot.post_message(msg)
            return
    msg = urban_dictionary.get_urban_dict()
    ctx.bot.post_message(msg)
