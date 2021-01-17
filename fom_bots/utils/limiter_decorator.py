from datetime import datetime
from enum import Enum
from functools import wraps
from random import randint

from groupme_bot import Context, EmojiAttachment

from storage.postgres import postgres_cursor


class Period(Enum):
    MINUTE = 1
    HOUR = 2
    DAY = 3


def get_current_period(period: Period):
    now = datetime.now()
    if period == Period.MINUTE:
        return now.strftime('%Y-%m-%d %H:%M')
    elif period == Period.HOUR:
        return now.strftime('%Y-%m-%d %H')
    elif period == Period.DAY:
        return now.strftime('%Y-%m-%d')


def with_limit(limit_id: str, max_calls: int, period: Period):
    def decorate(fn):
        @wraps(fn)
        def wrapper(ctx: Context):
            with postgres_cursor(commit=True) as cursor:
                cur_period = get_current_period(period)
                cursor.execute(
                    "SELECT calls FROM limits WHERE id = %s AND period = %s",
                    (limit_id, cur_period,)
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
                calls += 1
                fn(ctx)
                cursor.execute(
                    """
                    INSERT INTO limits(id, period, calls) 
                    VALUES(%s, %s, %s)
                    ON CONFLICT (id) 
                    DO 
                       UPDATE SET period = excluded.period, calls = excluded.calls;
                    """,
                    (limit_id, cur_period, calls)
                )

        return wrapper

    return decorate
