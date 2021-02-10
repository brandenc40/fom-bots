import re
from random import choice

from groupme_bot import Context

from constants import regex
from gateways import pirate
from utils.error_decorator import handle_exceptions
from constants.pirate import SONGS


@handle_exceptions
def insult(ctx: Context):
    msg = pirate.get_insult()
    ctx.bot.post_message(msg)


@handle_exceptions
def translate(ctx: Context):
    sr = re.search(regex.PIRATE_TRANSLATE + r'(.+)', ctx.callback.text)
    if sr:
        q_str = sr.group(1).strip()
        if q_str:
            msg = pirate.translate(q_str)
            ctx.bot.post_message(msg)
            return
    ctx.bot.post_message(pirate.get_insult())


@handle_exceptions
def sea_shanty(ctx: Context):
    ctx.bot.post_message(choice(SONGS))
