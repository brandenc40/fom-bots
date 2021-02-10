from groupme_bot import Bot

import config
from constants import regex
from handlers import bible

rukebot = Bot(
    "RukeBot",
    bot_id=config.RUKEBOT_ID,
    groupme_api_token=config.GROUPME_API_TOKEN,
    group_id=config.FOM_GROUP_ID
)

rukebot.add_callback_handler(regex.BIBLE_VERSE, bible.random_bible_verse)
rukebot.add_callback_handler(regex.BIBLE_IN_VANE, bible.name_in_vane)
rukebot.add_cron_job(bible.random_bible_verse, hour=9, timezone='America/Chicago')
