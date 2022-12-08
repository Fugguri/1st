from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards import *
from aiogram.dispatcher.storage import FSMContext
from main import dp, bot, users


@dp.message_handler(Text(equals="Начать сначала"), state="*")
@dp.message_handler(commands=['start'])  # начало работы бота
async def start(message: types.Message):
    users[message.from_user.id] = {}
    await message.answer(text="Расскажи, из какого ты города?", reply_markup=start_markup)


@ dp.message_handler(Text)
async def dont_allow_text(message: types.Message):

    await message.answer("Не понимаю!\nЧтобы начать нажми /start")
