from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from data_writer import add_items
from main import dp, bot, users
from asyncio import sleep
from pathlib import Path


class Resume(StatesGroup):
    full_name = State()
    phone = State()
    resume = State()


# @ dp.message_handler(Text(equals="Начать сначала"), state="*")
# async def dont_allow_text(message: types.Message, state: FSMContext):
#     current_state = state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.reply("Отменил\n/start чтобы начать сначала")


@dp.callback_query_handler(lambda call: call.data == 'Com NO')
async def resum(callback: types.CallbackQuery):
    users[callback.message.chat.id]["Общение"] = "Нет"
    await bot.send_message(chat_id=callback.message.chat.id, text='Тогда в этом департаменте мы не сможем предложить тебе вакансию😔\nРасскажи подробнее о себе и своем опыте. У нас есть вакансии в других отделах)')
    await sleep(1)
    await Resume.full_name.set()
    await bot.send_message(chat_id=callback.message.chat.id, text="Введите ФИО", reply_markup=clear_state())


@dp.callback_query_handler(lambda call: call.data == "other")
async def resum(callback: types.CallbackQuery):
    users[callback.message.chat.id]["Общение"] = "Да"
    await bot.send_message(chat_id=callback.message.chat.id, text='Расскажи о себе поподробнее и мы подберем для тебя подходящую вакансию☺️')
    await sleep(1)
    await Resume.full_name.set()
    await bot.send_message(chat_id=callback.message.chat.id, text="Введите ФИО", reply_markup=clear_state())


@ dp.message_handler(lambda message: message.text.count(" ") != 2 or message.text.isdigit(), state=Resume.full_name)
async def chech_name(message: types.Message, state: FSMContext):
    await message.reply("Введите имя фамилию и отчество.(должно получиться 3 слова")


@ dp.message_handler(state=Resume.full_name)
async def save_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["full_name"] = message.text
    await message.answer("Введите номер телефона")
    await Resume.next()


@ dp.message_handler(lambda message:  message.text.isdigit() and 8 > len(message.text) < 12, state=Resume.phone)
async def chech_age(message: types.Message, state: FSMContext):
    await message.reply("Введите реальный номер")


@ dp.message_handler(state=Resume.phone)
async def save_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone"] = message.text
    await message.answer("Прикрепите резюме")
    await Resume.next()


@ dp.message_handler(lambda message: message.content_type != "file", state=Resume.resume)
async def chech_age(message: types.Message, state: FSMContext):
    await message.reply("Прикрепите файл")


@dp.message_handler(content_types=[types.ContentType.DOCUMENT], state=Resume.resume)
async def save_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["id"] = message.from_user.id
        data["city"] = users[message.from_user.id]["Город"]
        data["age"] = "-"

        try:
            users[message.from_user.id]["Работал с клиентами"]
        except:
            users[message.from_user.id]["Работал с клиентами"] = []
        finally:
            data["clients"] = users[message.from_user.id]["Работал с клиентами"]
        try:
            users[message.from_user.id]["Навыки"]
        except:
            users[message.from_user.id]["Навыки"] = []
        finally:
            data["skills"] = users[message.from_user.id]["Навыки"]
        try:
            users[message.from_user.id]["Отделение"]
        except:
            users[message.from_user.id]["Отделение"] = []
        finally:
            data["departament"] = users[message.from_user.id]["Отделение"]
    add_items(data)
    await save_resume(message, state)
    await state.finish()
    await message.answer("Отлично✅\nМы вернемся с обратной связью в течении 3х рабочих дней (с 10.00 до 19.00)")


async def save_resume(message: types.Message, state: FSMContext):
    file_id = message.document.file_id
    # try:
    #     bot.get_file(file_id)
    #     print(type(bot.get_file))
    # except:
    #     await message.answer("Ошибка! Попробуйте другой файл")
    file = await bot.get_file(file_id)
    file_path = file.file_path
    async with state.proxy() as data:
        file_on_disk = Path(
            "Резюме/", f"{data['full_name'].replace(' ','_')}_id{message.from_user.id}.{message.document.mime_subtype}")
    await bot.download_file(file_path, destination=file_on_disk)
