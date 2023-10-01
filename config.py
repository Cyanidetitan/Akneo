import os
from telethon import TelegramClient

api_id = "10247139"
api_hash = "96b46175824223a33737657ab943fd6a"
bot_token = "6688322604:AAEUGfg6yN79Ib3_3FrBpF1HE00j2jB6-iI"

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
