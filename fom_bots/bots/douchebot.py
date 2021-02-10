from groupme_bot import Bot

import config
from constants import regex
from handlers import (
    groupme, mentions, xxx, insult,
    help, miscellaneous, urban_dictionary,
    gif
)

douchebot = Bot(
    "Douchebot",
    bot_id=config.DOUCHEBOT_ID,
    groupme_api_token=config.GROUPME_API_TOKEN,
    group_id=config.FOM_GROUP_ID
)

handlers = (
    (regex.DOUCHE, insult.random_insult),
    (regex.ALL, groupme.mention_all),
    (regex.COD, mentions.cod_time),
    (regex.FIFA, mentions.fifa_time),
    (regex.PGA, mentions.pga_time),
    (regex.QC, mentions.qc_fom),
    (regex.NSFW, xxx.nsfw),
    (regex.PORN, xxx.porn),
    (regex.HELP, help.show_help),
    (regex.HORN, miscellaneous.purple_pills),
    (regex.JORDAN, miscellaneous.flooring_america),
    (regex.SHAYNE, miscellaneous.baby_crying),
    (regex.URBAN, urban_dictionary.urban_dictionary_search),
    (regex.GIF, gif.search_gif)
)

for handler in handlers:
    douchebot.add_callback_handler(handler[0], handler[1])
