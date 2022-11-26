from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards import start_markup, communicate, client_experiens, ready_to_study, next_coll, a, get_inline_keyboard, clear_state
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from data_writer import add_items
storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage=storage)


users = {}


async def on_startup(_):
    print("Бот запущен")


async def on_shutdown(_):
    print("Бот остановлен")


@dp.message_handler(commands=['start'])  # начало работы бота
async def start(message: types.Message):
    users[message.from_user.id] = {}
    await message.answer(text="Из какого ты города?", reply_markup=start_markup)
   #  await message.delete()


class MyStatesGroup(StatesGroup):
    full_name = State()
    age = State()
    phone = State()


@ dp.message_handler(Text(equals="Очистить"), state="*")
async def dont_allow_text(message: types.Message, state: FSMContext):
    current_state = state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Отменил\n/start чтобы начать сначала")


@dp.callback_query_handler(lambda call: call.data == "next")
async def save(callback: types.CallbackQuery):
    await MyStatesGroup.full_name.set()
    await bot.send_message(chat_id=callback.message.chat.id, text="Введите ФИО", reply_markup=clear_state())


@ dp.callback_query_handler(lambda call: call.data.startswith('c'))
async def reg(callback: types.CallbackQuery):
    global number
    output = users[callback.message.chat.id]["Навыки"]
    if callback.data == 'c_servise':
        a = "Обслуживание и сервис"
        if a not in output:
            users[callback.message.chat.id]["Навыки"].append(a)
        else:
            output.remove(a)
            if users[callback.message.chat.id]["Навыки"]==[]:
                users[callback.message.chat.id]["Навыки"].append("-")
        await callback.message.edit_text(text=f"{' '.join(output)}", reply_markup=get_inline_keyboard())
        await callback.answer()

    if callback.data == 'c_tele_sales_b':
        a = "Телефонные продажи B2B"
        if a not in output:
            users[callback.message.chat.id]["Навыки"].append(a)
        else:
            output.remove(a)
            if users[callback.message.chat.id]["Навыки"]==[]:
                users[callback.message.chat.id]["Навыки"].append("-")
        await callback.message.edit_text(text=f"{' '.join(output)}", reply_markup=get_inline_keyboard())

    if callback.data == 'c_tele_sales_c':
        a = "Телефонные продажи B2C"
        if a not in output:
            users[callback.message.chat.id]["Навыки"].append(a)
        else:
            output.remove(a)
            if users[callback.message.chat.id]["Навыки"]==[]:
                users[callback.message.chat.id]["Навыки"].append("-")
        await callback.message.edit_text(text=f"{' '.join(output)}", reply_markup=get_inline_keyboard())

    if callback.data == 'c_direct_sales_b':
        a = "Прямые продажи B2B"
        if a not in output:
            users[callback.message.chat.id]["Навыки"].append(a)
        else:
            output.remove(a)
            if users[callback.message.chat.id]["Навыки"]==[]:
                users[callback.message.chat.id]["Навыки"].append("-")
        await callback.message.edit_text(text=f"{' '.join(output)}", reply_markup=get_inline_keyboard())

    if callback.data == 'c_direct_sales_c':
        a = "Прямые продажи B2C"
        if a not in output :
            users[callback.message.chat.id]["Навыки"].append(a)
        else:
            output.remove(a)
            if users[callback.message.chat.id]["Навыки"]==[]:
                users[callback.message.chat.id]["Навыки"].append("-")
        await callback.message.edit_text(text=f"{' '.join(output)}", reply_markup=get_inline_keyboard())

    if callback.data == 'c_form_accept':
        if "Телефонные продажи B2C" not in output:
            users[callback.message.chat.id]["Отделение"] = "Колл центр"
            await bot.send_message(chat_id=callback.message.chat.id,
                                   text="Приглашаем тебя пройти собеседование на вакансию сотрудника колл-центра! Для этого заполни форму ниже", reply_markup=next_coll)
        else:
            users[callback.message.chat.id]["Отделение"] = "Менеджер по продажам"
            await bot.send_message(chat_id=callback.message.chat.id,
                                   text="Приглашаем тебя пройти собеседование на вакансию менеджера по продажам! Для этого заполни форму ниже", reply_markup=next_coll)


@ dp.callback_query_handler()
async def city(callback: types.CallbackQuery):
    if callback.data == 'Москва' or callback.data == 'Санкт-Петербург':
        users[callback.message.chat.id]["Город"] = callback.data
        await bot.send_message(chat_id=callback.message.chat.id, text="Любишь общаться с людьми?", reply_markup=communicate)
        await callback.answer()
    elif callback.data == 'Другое':
        users[callback.message.chat.id]["Город"] = callback.data
        await bot.send_message(chat_id=callback.message.chat.id, text="В других городах нас нет, но в будущем мы обязательно придем:)")
        await callback.answer()
    elif callback.data == 'Com NO':
        users[callback.message.chat.id]["Общение"] = "Нет"
        await bot.send_message(chat_id=callback.message.chat.id, text='Тогда у нас нет подходяшей вакансии:(')
    elif callback.data == 'Com YES':
        users[callback.message.chat.id]["Общение"] = "Да"
        await bot.send_message(chat_id=callback.message.chat.id, text="Был ли у тебя опыт работы с клиентами?", reply_markup=client_experiens)
    elif callback.data == 'Study YES':
        users[callback.message.chat.id]["Готов обучаться"] = "Да"
        users[callback.message.chat.id]["Отделение"] = "Колл центр"
        users[callback.message.chat.id]["Навыки"] = []
        await bot.send_message(chat_id=callback.message.chat.id, text='Отлично, тогда тебе к нам!', reply_markup=next_coll)
    elif callback.data == 'Study NO':
        users[callback.message.chat.id]["Готов обучаться"] = "Нет"
        await bot.send_message(chat_id=callback.message.chat.id, text='Тогда у нас сейчас нет подходящей вакансии :(')
    elif callback.data == 'Cli NO':
        users[callback.message.chat.id]["Работал с клиентами"] = "Нет"
        await bot.send_message(chat_id=callback.message.chat.id, text='А хотел бы научиться?', reply_markup=ready_to_study)
    elif callback.data == 'Cli YES':
        users[callback.message.chat.id]["Работал с клиентами"] = "Да"
        users[callback.message.chat.id]["Навыки"] = []
        await bot.send_message(chat_id=callback.message.chat.id, text="Отметь все сферы, в которых у тебя есть опыт", reply_markup=get_inline_keyboard())


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
    await message.reply("Отлично, мы позвоним тебе в будний день с 10 до 19")
    add_items(data)


@ dp.message_handler(Text)
async def dont_allow_text(message: types.Message):

    await message.answer("Не понимаю!\nЧтобы начать нажми /start")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
