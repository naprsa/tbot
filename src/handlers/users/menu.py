from aiogram import types
from aiogram.dispatcher.filters import Command

from src.loader import dp
from src.keyboards.default.menu import menu


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Choose your good from menu below", reply_markup=menu)


@dp.message_handler(text="Potatos")
async def get_potatos(message: types.Message):
    await message.answer("Your choise is Potatos")


@dp.message_handler(text="Pepsi")
async def get_potatos(message: types.Message):
    await message.answer("Your choise is Pepsi")


@dp.message_handler(text="Cola")
async def get_potatos(message: types.Message):
    await message.answer("Your choise is Cola")
