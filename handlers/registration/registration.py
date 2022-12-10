from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from data_writer import add_items
from main import dp, bot, users
from asyncio import sleep
from ..others.others import start


@ dp.message_handler(Text(equals="Начать сначала"), state="*")
async def dont_allow_text(message: types.Message, state: FSMContext):
    current_state = state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Отменил")
    await start()


class MyStatesGroup(StatesGroup):
    full_name = State()
    age = State()
    phone = State()


@dp.callback_query_handler(lambda call: call.data == "next")
async def save(callback: types.CallbackQuery):
    await MyStatesGroup.full_name.set()
    await sleep(1)
    await bot.send_message(chat_id=callback.message.chat.id, text="Введите ФИО", reply_markup=clear_state())


@ dp.callback_query_handler(lambda call: call.data.startswith('c'))
async def reg_experience(callback: types.CallbackQuery):
    global number
    output = users[callback.message.chat.id]["Навыки"]
    if callback.data == 'c_servise':
        a = "Обслуживание и сервис"
        users[callback.message.chat.id]["Навыки"].append(a)
        if users[callback.message.chat.id]["Навыки"] == []:
            users[callback.message.chat.id]["Навыки"].append("-")

    if callback.data == 'c_tele_sales_b':
        a = "Телефонные продажи B2B"

        users[callback.message.chat.id]["Навыки"].append(a)

    if callback.data == 'c_tele_sales_c':
        a = "Телефонные продажи B2C"

        users[callback.message.chat.id]["Навыки"].append(a)

    if callback.data == 'c_direct_sales_b':
        a = "Прямые продажи B2B"
        users[callback.message.chat.id]["Навыки"].append(a)

    if callback.data == 'c_direct_sales_c':
        a = "Прямые продажи B2C"
        users[callback.message.chat.id]["Навыки"].append(a)

    if callback.data in ['c_servise', 'c_tele_sales_b', 'c_tele_sales_c', 'c_direct_sales_b']:
        users[callback.message.chat.id]["Отделение"] = "Колл центр"
        await bot.send_message(chat_id=callback.message.chat.id,
                               text="Приглашаем тебя пройти собеседование на вакансию сотрудника <b>колл-центра!</b>📞 \nДля этого заполни форму ниже")
    else:
        users[callback.message.chat.id]["Отделение"] = "Менеджер по продажам"
        await bot.send_message(chat_id=callback.message.chat.id,
                               text="Приглашаем тебя пройти собеседование на вакансию <b>менеджера по продажам!</b>💰 \nДля этого заполни форму ниже")
    await MyStatesGroup.full_name.set()
    await bot.send_message(chat_id=callback.message.chat.id, text="Введите ФИО", reply_markup=clear_state())


@ dp.callback_query_handler(lambda call: call.data == 'Study YES')
async def reg(callback: types.CallbackQuery):
    users[callback.message.chat.id]["Готов обучаться"] = "Да"
    users[callback.message.chat.id]["Отделение"] = "Колл центр"
    users[callback.message.chat.id]["Навыки"] = []
    with open("hand.gif", "rb") as gif:
        await bot.send_animation(chat_id=callback.message.chat.id, animation=gif, caption='Отлично, тогда тебе к нам!\nПриглашаем тебя пройти собеседование на вакансию сотрудника <b>колл-центра!</b>📞\nДля этого заполни форму ниже')
    await MyStatesGroup.full_name.set()

    await bot.send_message(chat_id=callback.message.chat.id, text="Введите ФИО", reply_markup=clear_state())


@ dp.message_handler(lambda message: message.text.count(" ") != 2 or message.text.isdigit(), state=MyStatesGroup.full_name)
async def chech_name(message: types.Message, state: FSMContext):
    await message.reply("Введите имя фамилию и отчество.(должно получиться 3 слова")


@ dp.message_handler(state=MyStatesGroup.full_name)
async def save_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["full_name"] = message.text
    await message.answer("Введите возраст")
    await MyStatesGroup.next()


@ dp.message_handler(lambda message: not message.text.isdigit() or float(message.text) > 100, state=MyStatesGroup.age)
async def chech_age(message: types.Message, state: FSMContext):
    await message.reply("Введите реальный возраст(цифрами)")


@ dp.message_handler(state=MyStatesGroup.age)
async def save_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = message.text
    await message.answer("Введите номер телефона")
    await MyStatesGroup.next()


@ dp.message_handler(lambda message: not message.text.isdigit() or 8 < len(message.text) > 12, state=MyStatesGroup.phone)
async def chech_age(message: types.Message, state: FSMContext):
    await message.reply("Введите реальный номер")


@ dp.message_handler(state=MyStatesGroup.phone)
async def save_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone"] = message.text
        data["id"] = message.from_user.id
        data["city"] = users[message.from_user.id]["Город"]
        data["clients"] = users[message.from_user.id]["Работал с клиентами"]
        try:
            data["skills"] = users[message.from_user.id]["Навыки"]
        except ConnectionAbortedError:
            users[message.from_user.id]["Навыки"] = []
        finally:
            data["skills"] = users[message.from_user.id]["Навыки"]
        try:
            data["departament"] = users[message.from_user.id]["Отделение"]
        except ConnectionAbortedError:
            users[message.from_user.id]["Отделение"] = []
        finally:
            data["departament"] = users[message.from_user.id]["Отделение"]
    await state.finish()
    await message.answer("Отлично✅\nМы вернемся с обратной связью в течение 3-х рабочих дней (с 10.00 до 19.00)")
    add_items(data)
