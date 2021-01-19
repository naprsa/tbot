import io

from aiogram import types
from aiogram.dispatcher.filters import Command, AdminFilter

from src.loader import dp, bot


@dp.message_handler(Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(msg: types.Message):
    source_msg = msg.reply_to_message
    photo = source_msg.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(path_or_bytesio=photo)
    # await bot.set_chat_photo(chat_id=msg.chat.id, photo=input_file)
    await msg.chat.set_photo(photo=input_file)
