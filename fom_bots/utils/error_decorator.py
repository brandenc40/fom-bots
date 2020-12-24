from functools import wraps

from groupme_bot import Context

from config import logger


def handle_exceptions(f):
    @wraps(f)
    def wrapper(ctx: Context):
        try:
            f()
        except Exception as e:
            logger.error(str(e), exc_info=e)
            ctx.bot.post_message("Shits broken... The function `{}` threw this error: {}".format(f.__name__, str(e)))

    return wrapper
