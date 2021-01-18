from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link

from filters import IsPrivate
from re import compile

from loader import dp


@dp.message_handler(
    CommandStart(deep_link=compile(r"\d\d\d"), encoded=True), IsPrivate()
)
async def bot_start_deeplink(message: types.Message):
    deep_link_args = message.get_args()
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"
        f"Вы находитесь в личной переписке. \n"
        f"В вашей команде есть диплинк. \n"
        f"Вы передали аргумент {deep_link_args}. \n"
    )


@dp.message_handler(CommandStart(deep_link=None), IsPrivate())
async def bot_start_deeplink(message: types.Message):

    deep_link = await get_start_link("123", encode=True)

    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"
        f"Вы находитесь в личной переписке. \n"
        f"В вашей команде есть нет диплинка. \n"
        f"Ссылка на диплинк {deep_link}. \n"
    )
