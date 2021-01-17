from groupme_bot import Application

from bots.douchebot import douchebot
from bots.rukebot import rukebot
from storage.postgres import init_db

app = Application()

app.add_bot(douchebot, callback_path='/douchebot')
app.add_bot(rukebot, callback_path='/rukebot')

init_db()
