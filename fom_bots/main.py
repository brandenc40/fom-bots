import os

from groupme_bot import Router

from bots.douchebot import douchebot
from bots.rukebot import rukebot

router = Router()

router.add_bot(douchebot, callback_path='/douchebot')
router.add_bot(rukebot, callback_path='/rukebot')

router.run(
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 33507)),
    debug=bool(os.environ.get('DEBUG', False))
)
