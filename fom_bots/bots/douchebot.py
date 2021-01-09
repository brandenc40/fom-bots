from groupme_bot import Bot

import config
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

douchebot.add_callback_handler(r'douche', insult.random_insult)
douchebot.add_callback_handler(r'^[\\|\/]all', groupme.mention_all)
douchebot.add_callback_handler(r'^[\\|\/]codtime', mentions.cod_time)
douchebot.add_callback_handler(r'^[\\|\/]fifatime', mentions.fifa_time)
douchebot.add_callback_handler(r'^[\\|\/]pgatime', mentions.pga_time)
douchebot.add_callback_handler(r'^[\\|\/]qcfom', mentions.qc_fom)
douchebot.add_callback_handler(r'^[\\|\/]nsfw', xxx.nsfw)
douchebot.add_callback_handler(r'^[\\|\/]porn', xxx.porn)
douchebot.add_callback_handler(r'^[\\|\/]help', help.show_help)
douchebot.add_callback_handler(r'^[\\|\/]horn', miscellaneous.purple_pills)
douchebot.add_callback_handler(r'^[\\|\/]gagme', miscellaneous.flooring_america)
douchebot.add_callback_handler(r'^[\\|\/]shayne', miscellaneous.baby_crying)
douchebot.add_callback_handler(r'^[\\|\/]urban', urban_dictionary.urban_dictionary_search)
douchebot.add_callback_handler(r'^[\\|\/]gif', gif.search_gif)
