from aiogram import types

from src.filters import IsPrivate
from src.loader import dp

from src.data.config import admins


@dp.message_handler(IsPrivate(), text="secret", user_id=admins)
async def admin_chat_secret(message: types.Message):
    await message.answer(
        "Это секретное сообщение, вызванное одним из администраторов"
        "в личнеой переписке"
    )
