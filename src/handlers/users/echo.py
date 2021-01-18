from aiogram import types
from aiogram.dispatcher.filters import Command
from loguru import logger
from src.loader import dp

from src.utils.misc import rate_limit
from src.utils.db_api.user import User


@rate_limit(limit=3)
@dp.message_handler(Command("mid"))
async def bot_echo(message: types.Message, user: User):
    logger.debug(user)
    await message.answer(
        f"UserID: {message.from_user.id}" f"User from middleware: {user.__dict__}"
    )
