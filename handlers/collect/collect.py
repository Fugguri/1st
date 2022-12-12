from aiogram import types
from main import dp, bot, users
from config import TOKEN_API
from keyboards import *
from asyncio import sleep


@ dp.callback_query_handler()
async def city(callback: types.CallbackQuery):
    if callback.data == 'Москва' or callback.data == 'Санкт-Петербург':
        await callback.message.answer(text="👋")
        if not users[callback.message.chat.id]:
            users[callback.message.chat.id] = {}

        users[callback.message.chat.id]["Город"] = callback.data
        await sleep(2)
        await bot.send_message(chat_id=callback.message.chat.id, text="В нашем коммерческом департаменте тебя ждет много общения с клиентами💪\nРасскажи, тебе нравится общаться с людьми?", reply_markup=communicate)

    elif callback.data == 'Другое':
        if not users[callback.message.chat.id]:
            users[callback.message.chat.id] = {}
        users[callback.message.chat.id]["Город"] = callback.data
        await bot.send_message(chat_id=callback.message.chat.id, text="В этом городе нас нет, но в будущем мы обязательно придем.☺️")

        """Добавить форму сбора данных"""

    elif callback.data == 'Com YES':
        if not users[callback.message.chat.id]:
            users[callback.message.chat.id] = {}
        users[callback.message.chat.id]["Общение"] = "Да"
        await bot.send_message(chat_id=callback.message.chat.id, text="Был ли у тебя опыт работы с клиентами?", reply_markup=client_experiens)

    elif callback.data == 'Study NO':
        if not users[callback.message.chat.id]:
            users[callback.message.chat.id] = {}
        users[callback.message.chat.id]["Готов обучаться"] = "Нет"
        await bot.send_message(chat_id=callback.message.chat.id, text='Тогда у нас сейчас нет подходящей вакансии :(')
    elif callback.data == 'Cli NO':
        if not users[callback.message.chat.id]:
            users[callback.message.chat.id] = {}
        users[callback.message.chat.id]["Работал с клиентами"] = "Нет"
        await bot.send_message(chat_id=callback.message.chat.id, text='А хотел бы научиться?', reply_markup=ready_to_study)
    elif callback.data == 'Cli YES':
        if not users[callback.message.chat.id]:
            users[callback.message.chat.id] = {}
        users[callback.message.chat.id]["Работал с клиентами"] = "Да"
        users[callback.message.chat.id]["Навыки"] = []
        await bot.send_message(chat_id=callback.message.chat.id, text="Отметь сферу, в которой у тебя есть опыт", reply_markup=get_inline_keyboard())
