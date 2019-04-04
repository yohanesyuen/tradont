from common.config import Config

import logging

logger = logging.getLogger(__name__)

config_filename = "v20.cfg"
config = Config()

try:
    config.load(config_filename)
    logger.info("Loaded config: {}".format(config_filename))
except:
    logger.error("Config file '{}' doesn't exist, starting with defaults.".format(config_filename))

active_account = config.active_account
ctx = config.create_context()

def get_active_account():
    return active_account

__all__ = [
        'ctx',
        'get_active_account']

