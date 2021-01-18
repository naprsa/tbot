from loguru import logger

from src.keyboards.inline.callback_datas import buy_callback
from src.keyboards.inline.choices_buttons import choices, pear_keyboard
from src.loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer(
        text="На продажу есть 2 товара: 5 яблок и 3 груша \n"
        "Если ничего не выбрали - нажимите 'отмена'",
        reply_markup=choices,
    )


@dp.callback_query_handler(buy_callback.filter(item_name="pear"))
async def buying_pear(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=10)
    logger.info(f"callback data: {call.data}")
    logger.info(f"callback data dict: {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(
        f"Вы выбюрали купить грушу,  всего {quantity}", reply_markup=pear_keyboard
    )


@dp.callback_query_handler(text="cancel")
async def cancel(call: types.CallbackQuery):
    await call.answer("Вы нажали отмена", show_alert=True)
    await call.message.edit_reply_markup()
