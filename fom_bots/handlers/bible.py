from groupme_bot import Context

from gateways import bible
from utils.error_decorator import handle_exceptions


@handle_exceptions
def random_bible_verse(ctx: Context):
    verse = bible.random_bible_verse()
    ctx.bot.post_message(verse)
