from random import choice

from groupme_bot import Context

from gateways import bible
from utils.error_decorator import handle_exceptions

NAME_IN_VANE_RESPONSES = [
    "Leave him out of this.",
    "Watch your tongue, you heathen.",
    "May the Holy Name of God be blessed. Begone satan.",
    "Blessed be thy name.",
    "You're going to Hell.",
    "The Bible says don't say that."
]


@handle_exceptions
def random_bible_verse(ctx: Context):
    verse = bible.random_bible_verse()
    ctx.bot.post_message(verse)


def name_in_vane(ctx: Context):
    ctx.bot.post_message(choice(NAME_IN_VANE_RESPONSES))
