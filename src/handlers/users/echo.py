from aiogram import types
from src.loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(message.from_user.id)