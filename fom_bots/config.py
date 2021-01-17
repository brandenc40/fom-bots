import os
import logging

from starlette.config import Config


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Config will be read from environment variables and/or ".env" files.
config = Config(os.path.join(BASE_DIR, ".env"))

# env secrets
DOUCHEBOT_ID = config('DOUCHEBOT_ID', cast=str, default="")
FOM_GROUP_ID = config('FOM_GROUP_ID', cast=str, default="")
GROUPME_API_TOKEN = config('GROUPME_API_TOKEN', cast=str, default="")
RUKEBOT_ID = config('RUKEBOT_ID', cast=str, default="")
TENOR_API = config('TENOR_API', cast=str, default="")
DATABASE_URL = config('DATABASE_URL', cast=str, default="")

logger = logging.getLogger('fom-bots')
