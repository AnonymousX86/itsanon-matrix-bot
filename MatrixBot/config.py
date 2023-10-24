# -*- coding: utf-8 -*-
from os import getenv

from dotenv import load_dotenv

if __name__ == '__main__':
    pass
else:
    load_dotenv()

HOMESERVER_URL = getenv('HOMESERVER_URL')
BOT_LOGIN = getenv('BOT_LOGIN')
BOT_PASSWORD = getenv('BOT_PASSWORD')

PREFIX = getenv('PREFIX', '!')
