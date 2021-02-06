from groupme_bot import Bot

import config
from handlers import pirate

pirate_bot = Bot(
    "PirateBot",
    bot_id=config.PIRATEBOT_ID,
    groupme_api_token=config.GROUPME_API_TOKEN,
    group_id=config.FOM_GROUP_ID
)

pirate_bot.add_callback_handler(r'^[\\\/]pirate', pirate.translate)
pirate_bot.add_callback_handler(r'\b(sea|ship|boat|argh|arghh|loot|plunder|pirate|cunt)\b', pirate.insult)
pirate_bot.add_callback_handler(r'\b(shanty)\b', pirate.sea_shanty)
