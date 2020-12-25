from groupme_bot import Context

from gateways import tenor
from utils.error_decorator import handle_exceptions


@handle_exceptions
def search_gif(ctx: Context):
    gif_url = tenor.search_gif(ctx.callback.text)
    ctx.bot.post_message(gif_url)
