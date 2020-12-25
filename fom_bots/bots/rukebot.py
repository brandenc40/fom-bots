import os

from groupme_bot import Bot

from handlers import bible

rukebot = Bot(
    "RukeBot",
    bot_id=os.environ.get('RUKEBOT_ID'),
    groupme_api_token=os.environ.get('GROUPME_API_TOKEN'),
    group_id=os.environ.get('FOM_GROUP_ID')
)

rukebot.add_callback_handler(r'^\\bible', bible.random_bible_verse)
rukebot.add_callback_handler(r'god|jesus|omg|lord', bible.name_in_vane)
rukebot.add_cron_job(bible.random_bible_verse, hour=9, timezone='America/Chicago')
