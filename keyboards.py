from aiogram.types import ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton

# клавиатуры

start_markup = InlineKeyboardMarkup(row_width=2)  # Клавиатура выбора города
button1 = InlineKeyboardButton(
    "🏙Москва", callback_data="Москва")
button2 = InlineKeyboardButton(
    "🌉Санкт-Петербург", callback_data='Санкт-Петербург')
button3 = InlineKeyboardButton(
    "🇷🇺Другое", callback_data='Другое')

start_markup.add(button1, button2, button3)

communicate = InlineKeyboardMarkup(row_width=2)  # Любишь общаться?
yes_botton = InlineKeyboardButton(
    "👍", callback_data='Com YES')
no_button = InlineKeyboardButton(
    "👎", callback_data='Com NO')
reset = form_accept = InlineKeyboardButton(
    "Начать сначала", callback_data='reset')
communicate.add(yes_botton, no_button, reset)

client_experiens = InlineKeyboardMarkup(row_width=2)  # Опыт работы с клиентами
yes_botton = InlineKeyboardButton(
    "👍", callback_data='Cli YES')
no_button = InlineKeyboardButton(
    "👎", callback_data='Cli NO')
reset = form_accept = InlineKeyboardButton(
    "Начать сначала", callback_data='reset')
client_experiens.add(yes_botton, no_button, reset)

# Готов ли учиться обучаться работе с клиентами
ready_to_study = InlineKeyboardMarkup(row_width=2)
yes_botton = InlineKeyboardButton(
    "👍", callback_data='Study YES')
no_button = InlineKeyboardButton(
    "👎", callback_data='Study NO')
reset = form_accept = InlineKeyboardButton(
    "Начать сначала", callback_data='reset')
ready_to_study.add(yes_botton, no_button, reset)

# опрос по навыкам

next_coll = InlineKeyboardMarkup()
next = InlineKeyboardButton(text="Дальше", callback_data="next")
next_coll.add(next)
a = ReplyKeyboardRemove()


def get_inline_keyboard() -> InlineKeyboardMarkup:
    experience = InlineKeyboardMarkup(row_width=1)
    servise = InlineKeyboardButton(
        "☺️Обслуживание и сервис(магазины, приемы обращений, рестораны, консультирование", callback_data='c_servise')
    tele_sales_b = InlineKeyboardButton(
        "🤝Телефонные продажи B2B", callback_data='c_tele_sales_b')
    tele_sales_c = InlineKeyboardButton(
        "📲Телефонные продажи B2C", callback_data='c_tele_sales_c')
    direct_sales_b = InlineKeyboardButton(
        "✒️Прямые продажи B2B", callback_data='c_direct_sales_b')
    direct_sales_c = InlineKeyboardButton(
        "💼Прямые продажи B2C", callback_data='c_direct_sales_c')
    form_accept = InlineKeyboardButton(
        "👤Другое", callback_data='other')
    reset = InlineKeyboardButton(
        "Начать сначала", callback_data='reset')
    experience.add(servise, tele_sales_b, tele_sales_c,
                   direct_sales_b, direct_sales_c, form_accept, reset)

    return experience


def clear_state() -> InlineKeyboardMarkup:
    experience = ReplyKeyboardMarkup(resize_keyboard=True)
    kb = KeyboardButton("Начать сначала")
    experience.add(kb)

    return experience
