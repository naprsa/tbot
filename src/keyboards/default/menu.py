from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Potatos")],
        [KeyboardButton(text="Pepsi"), KeyboardButton(text="Cola")],
    ],
    resize_keyboard=True,
)
