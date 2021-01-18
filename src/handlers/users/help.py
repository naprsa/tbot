from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from src.loader import dp

from src.utils.misc import rate_limit


@rate_limit(limit=10)
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ["Список команд: ", "/start - Начать диалог", "/help - Получить справку"]
    await message.answer("\n".join(text))
