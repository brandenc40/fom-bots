import logging

logging.basicConfig(
    format='%(levelname)s %(asctime)s: %(message)s',
    level=logging.ERROR
)
logger = logging.getLogger('fom-bots')
