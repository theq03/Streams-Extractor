#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1629412971:AAEdl1_xmnuR3dC3jZ3uW-kwlms9J19FmeE")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "2572163"))
    API_HASH = os.environ.get("API_HASH", "deede80ddff7842db6c90b5715635142")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1292898087").split())
    
