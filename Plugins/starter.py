from Helper.helper import start_text, help_text
from config import bot
from telethon import events

class start():

    @bot.on(events.NewMessage(pattern=r"^/start$|^/start@Gojogod_robot"))
    async def event_handler_start(event):
        await bot.send_message(
            event.chat_id,
            start_text,
            file='https://mi-link.herokuapp.com/dl/0/AgADSAcAAk-hwVQ.mp4'
        )

    @bot.on(events.NewMessage(pattern=r"^/help$|^/help@Gojogod_robot"))
    async def event_handler_help(event):
        await bot.send_message(
            event.chat_id,
            help_text
            )

    @bot.on(events.NewMessage(pattern="/channel"))
    async def event_handler_source(event):
        await bot.send_message(
            event.chat_id,
            '[Our channel](https://t.me/latest_ongoing_airing_anime)\n Your support is appreciated!'
        )
    
