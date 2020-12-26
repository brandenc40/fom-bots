from random import choice

from groupme_bot import Context

from gateways import bible
from utils.error_decorator import handle_exceptions

NAME_IN_VANE_RESPONSES = [
    "Leave him out of this.",
    "Watch your tongue, you heathen.",
    "May the Holy Name of God be blessed. Begone satan.",
    "Hey friend, don’t take the Lord’s Name in vain! It ain’t good for you!",
    "Blessed be thy name.",
    "I notice you talk about God/Jesus a lot. I'm curious to know what you think about God, exactly? I'd love to "
    "discuss it!",
    "You're going to Hell.",
    "The Bible says don't say that.",
    "You must not misuse the name of the LORD your God. The LORD will not let you go unpunished if you misuse his "
    "name. - Deuteronomy 5:10-11",
    "Do not bring shame on the name of your God by using it to swear falsely. I am the LORD. - Leviticus 19:12"
]


@handle_exceptions
def random_bible_verse(ctx: Context):
    verse = bible.random_bible_verse()
    ctx.bot.post_message(verse)


def name_in_vane(ctx: Context):
    ctx.bot.post_message(choice(NAME_IN_VANE_RESPONSES))
