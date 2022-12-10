from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards import *
from aiogram.dispatcher.storage import FSMContext
from main import dp, bot, users


@ dp.message_handler(Text(equals="Начать сначала"), state="*")
@dp.callback_query_handler(lambda call: call.data == "reset")
@dp.message_handler(commands=['start'])  # начало работы бота
async def start(message: types.Message, callback: types.CallbackQuery = None, state="*",):
    current_state = state.get_state()
    if current_state is None:
        pass
    else:
        await state.finish()
    if message:
        users[message.from_user.id] = {}
        await bot.send_message(chat_id=message.from_user.id, text="Расскажи, из какого ты города?", reply_markup=start_markup)
    elif callback:
        users[callback.from_user.id] = {}
        await bot.send_message(chat_id=message.from_user.id, text="Расскажи, из какого ты города?", reply_markup=start_markup)


@ dp.message_handler(Text)
async def dont_allow_text(message: types.Message):

    await message.answer("Не понимаю!\nЧтобы начать нажми /start")


async def send__to_admin():
    ADMIN_ID = 248184623
    bot.send_document(chat_id=ADMIN_ID,)
