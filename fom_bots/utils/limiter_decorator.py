from datetime import datetime
from enum import Enum
from functools import wraps
from random import randint
from typing import Callable

from groupme_bot import Context, EmojiAttachment
from pytz import timezone

from storage.postgres import postgres_cursor


class Period(Enum):
    MINUTE = 1
    HOUR = 2
    DAY = 3


def get_current_period(period: Period):
    now = datetime.now(timezone('America/Chicago'))
    if period == Period.MINUTE:
        return now.strftime('%Y-%m-%d %H:%M')
    elif period == Period.HOUR:
        return now.strftime('%Y-%m-%d %H')
    elif period == Period.DAY:
        return now.strftime('%Y-%m-%d')


def with_limit(limit_id: str, max_calls: int, period: Period):
    def decorate(fn: Callable):
        @wraps(fn)
        def wrapper(ctx: Context):
            l_id = limit_id + ctx.bot.bot_name
            cur_period = get_current_period(period)
            with postgres_cursor(commit=True) as cursor:
                cursor.execute(
                    "SELECT calls FROM limits WHERE id = %s AND period = %s",
                    (l_id, cur_period,)
                )
                out = cursor.fetchone()
                calls = 0
                if out is not None and len(out) == 1:
                    calls = out[0]
                    if calls == max_calls:
                        ctx.bot.post_message(
                            f"You reached your fucking limit, no more than "
                            f"{max_calls} per {period.name.lower()} are allowed. *",
                            [EmojiAttachment("*", [[1, randint(1, 60)]])]
                        )
                        return
                fn(ctx)
                calls += 1
                cursor.execute(
                    """
                    INSERT INTO limits(id, period, calls)
                    VALUES(%s, %s, %s)
                    ON CONFLICT (id) DO UPDATE
                    set
                        period = EXCLUDED.period,
                        calls = EXCLUDED.calls;
                    """,
                    (l_id, cur_period, calls)
                )

        return wrapper

    return decorate
