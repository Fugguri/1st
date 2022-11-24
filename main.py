from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards import start_markup, communicate, client_experiens, ready_to_study, next_coll, a, get_inline_keyboard, clear_state
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext

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
    users[message.chat.id] = {}
    await message.answer(text="Из какого ты города?", reply_markup=start_markup)
   #  await message.delete()

number = ""


class MyStatesGroup(StatesGroup):
    full_name = State()
    age = State()
    phone = State()


@ dp.message_handler(Text(equals="Очистить"), state="*")
async def dont_allow_text(message: types.Message, state: FSMContext):
    current_state = state.get_state()
    if current_state is None:
        return

    await message.reply("Отменил")
    await state.finish()


@dp.callback_query_handler(lambda call: call.data.startswith('c'))
async def reg(callback: types.CallbackQuery):
    global number
    output = users[callback.message.chat.id]["Навыки"]
    if callback.data == 'c_servise':
        a = "Обслуживание и сервис"
        if a not in output:
          users[callback.message.chat.id]["Навыки"].append(a)
        elif :
          output.remove(a)
      
        await callback.message.edit_text(text=f"{output}", reply_markup=get_inline_keyboard())
        await callback.answer()
    if callback.data == 'c_tele_sales_b':
        users[callback.message.chat.id]["Навыки"].append(
            "Телефонные продажи B2B")
        number += "Телефонные продажи B2B\n"
        await callback.message.edit_text(text=f"{number}", reply_markup=get_inline_keyboard())
    if callback.data == 'c_tele_sales_c':
        users[callback.message.chat.id]["Навыки"].append(
            "Телефонные продажи B2C")
        number += "Телефонные продажи B2C\n"
        await callback.message.edit_text(text=f"{number}", reply_markup=get_inline_keyboard())
    if callback.data == 'c_direct_sales_b':
        users[callback.message.chat.id]["Навыки"].append(
            "Прямые продажи B2B")
        number += "Прямые продажи B2B\n"
        await callback.message.edit_text(text=f"{number}", reply_markup=get_inline_keyboard())
    if callback.data == 'c_direct_sales_c':
        users[callback.message.chat.id]["Навыки"].append(
            "Прямые продажи B2C")
        number += "Прямые продажи B2C\n"
        await callback.message.edit_text(text=f"{number}", reply_markup=get_inline_keyboard())
    if callback.data == 'c_form_accept':
        for i in users:
            print(users)


@dp.callback_query_handler()
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


@ dp.message_handler(Text(equals="Дальше"))
async def save(message: types.Message):
    await MyStatesGroup.full_name.set()
    await message.answer("Введите ФИО", reply_markup=clear_state())
    await MyStatesGroup.next()


@dp.message_handler(state=MyStatesGroup.age)
async def save_age(message: types.Message, state: FSMContext):
    await MyStatesGroup.next()
    await message.reply("Введите возраст")


@dp.message_handler(state=MyStatesGroup.phone)
async def save_age(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply("Введите номер телефона")


@ dp.message_handler(Text)
async def dont_allow_text(message: types.Message):

    await message.answer("Не понимаю!\nДля чтобы начать нажми /start")
    print(users)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
