from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_datas import buy_callback

choices = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Купить яблоки",
                callback_data=buy_callback.new(item_name="apple", quantity=3),
            ),
            InlineKeyboardButton(
                text="Купить Груши",
                callback_data=buy_callback.new(item_name="pear", quantity=3),
            ),
        ],
        [
            InlineKeyboardButton(
                text="Отмена",
                callback_data="cancel",
            ),
        ],
    ],
)


pear_keyboard = InlineKeyboardMarkup()
PEAR_LINK = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRx8wYEt_VU4G081ShajiNDfFZayXf8Jk-WnQ&usqp=CAU"
pear_link = InlineKeyboardButton(text="Купи тут", url=PEAR_LINK)
pear_keyboard.insert(pear_link)
