from aiogram import types
from aiogram.dispatcher.filters import Command
from loguru import logger
from src.loader import dp
from aiogram.utils.markdown import (
    hbold,
    hcode,
    hitalic,
    hunderline,
    hstrikethrough,
    hlink,
    hpre,
)


html_text = "\n".join(
    [
        "Привет, " + hbold("Сирежа"),
        "Как говорится:",
        hitalic("Волков боятся - в лес не ходить!"),
        "",
        "но мы не боимся дать отпор! " + hstrikethrough("Что тебе нужно?"),
        "Все это чистая хтмлуйня! ",
        "Узнай про себя кое что новое " + hlink("тут", "http://ya.ru"),
        "и нимножко коды: "
        + hpre(
            "from aiogram.dispatcher.filters import Command;from loguru import logger;from src.loader import dp;from aiogram.utils.markdown import hbold, hcode",
            sep=";",
        ),
    ]
)


@dp.message_handler(Command("format"))
async def bot_echo(message: types.Message):
    await message.answer(html_text)
