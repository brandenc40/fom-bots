from groupme_bot import Context

from utils.error_decorator import handle_exceptions


@handle_exceptions
def mention_all(ctx: Context):
    ctx.bot.mention_all()
