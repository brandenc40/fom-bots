from groupme_bot import Bot

import config
from constants import regex
from handlers import pirate

pirate_bot = Bot(
    "PirateBot",
    bot_id=config.PIRATEBOT_ID,
    groupme_api_token=config.GROUPME_API_TOKEN,
    group_id=config.FOM_GROUP_ID
)

pirate_bot.add_callback_handler(regex.PIRATE_TRANSLATE, pirate.translate)
pirate_bot.add_callback_handler(regex.PIRATE_INSULT, pirate.insult)
pirate_bot.add_callback_handler(regex.PIRATE_SHANTY, pirate.sea_shanty)
