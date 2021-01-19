from aiogram import types


USERS_COMMANDS = [
    types.BotCommand("start", "Start bot"),
    types.BotCommand("help", "Help"),
    types.BotCommand("test", "Пройти тест"),
    types.BotCommand("mid", "middleware"),
    types.BotCommand("items", "items"),
]

GROUPS_COMMANDS = [
    types.BotCommand("set_photo", "Set group image"),
    types.BotCommand("set_title", "Set group title"),
    types.BotCommand("set_description", "Set group description"),
    types.BotCommand("ro", "Set Read Only"),
    types.BotCommand("unro", "Unset Read Only"),
    types.BotCommand("ban", "Ban"),
    types.BotCommand("uban", "Unan"),
]


async def set_default_commands(dp):
    await dp.bot.set_my_commands(USERS_COMMANDS + GROUPS_COMMANDS)
