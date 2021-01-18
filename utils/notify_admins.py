from loguru import logger
from aiogram import Dispatcher
from data.config import admins


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Bot started")
        except Exception as err:
            logger.debug(err)


logger.debug("That's it, beautiful and simple logging!")
