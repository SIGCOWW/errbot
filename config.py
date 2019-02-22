import logging
import os

if 'SLACK_TOKEN' in os.environ:
    BACKEND = 'Slack'
    BOT_IDENTITY = {'token': os.environ['SLACK_TOKEN']}
else:
    BACKEND = 'Text'

BOT_DATA_DIR = './data'
os.mkdir(BOT_DATA_DIR)
BOT_EXTRA_PLUGIN_DIR = './plugins'

BOT_LOG_FILE = './errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@lrks', )
