from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from src.loader import dp
from aiogram import types
from src.states import Test


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(str(data))
    await message.answer(
        "вы начали тестирование. \n" "Вопрос 1. \n\n" "вы часто занимаетесь херней?"
    )

    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # await state.update_data(answer1=answer)
    # await state.update_data({"answer1": answer})

    async with state.proxy() as data:
        data["answer1"] = answer

    await message.answer("Вопрос 2. \n\n" "Сколько этой херни вам действтельно нужно?")
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q1(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data["answer2"] = message.text

    data = await state.get_data()
    await message.answer("Спасибо за ответы!")
    await message.answer(str(data))
    # await state.finish()
    await state.reset_state(with_data=False)
