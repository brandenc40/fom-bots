import logging

from starlette.config import Config

# Config will be read from environment variables and/or ".env" files.
config = Config(".env")

# env secrets
DOUCHEBOT_ID = config('DOUCHEBOT_ID', cast=str)
FOM_GROUP_ID = config('FOM_GROUP_ID', cast=str)
GROUPME_API_TOKEN = config('GROUPME_API_TOKEN', cast=str)
RUKEBOT_ID = config('RUKEBOT_ID', cast=str)
TENOR_API = config('TENOR_API', cast=str)

logger = logging.getLogger('fom-bots')
