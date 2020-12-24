from random import randint

from groupme_bot import Context

from constants.insults import INSULTS
from gateways.insult import get_insult
from utils.error_decorator import handle_exceptions


@handle_exceptions
def random_insult(ctx: Context):
    try:
        msg = get_insult('comeback')
    except Exception:
        val = randint(0, len(INSULTS) - 1)
        msg = INSULTS[val]
    ctx.bot.post_message(msg)
