from aiogram.types import ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton

# клавитатуры
start_markup = InlineKeyboardMarkup()  # Клавиатура выбора города
button1 = InlineKeyboardButton(
    "Москва", callback_data="Москва")
button2 = InlineKeyboardButton(
    "Санкт-Петербург", callback_data='Санкт-Петербург')
button3 = InlineKeyboardButton(
    "Другое", callback_data='Другое')
start_markup.add(button1, button2, button3)


communicate = InlineKeyboardMarkup()  # Любишь общаться?
yes_botton = InlineKeyboardButton(
    "Да", callback_data='Com YES')
no_button = InlineKeyboardButton(
    "Нет", callback_data='Com NO')
communicate.add(yes_botton, no_button)

client_experiens = InlineKeyboardMarkup()  # Опыт работы с клиентами
yes_botton = InlineKeyboardButton(
    "Да", callback_data='Cli YES')
no_button = InlineKeyboardButton(
    "Нет", callback_data='Cli NO')
client_experiens.add(yes_botton, no_button)

# Готов ли учиться обучаться работе с клиентами
ready_to_study = InlineKeyboardMarkup()
yes_botton = InlineKeyboardButton(
    "Да", callback_data='Study YES')
no_button = InlineKeyboardButton(
    "Нет", callback_data='Study NO')
ready_to_study.add(yes_botton, no_button)

# опрос по навыкам


next_coll = InlineKeyboardMarkup()
next = InlineKeyboardButton(text="Дальше", callback_data="next")
next_coll.add(next)
a = ReplyKeyboardRemove()


def get_inline_keyboard() -> InlineKeyboardMarkup:
    experience = InlineKeyboardMarkup(row_width=1)
    servise = InlineKeyboardButton(
        "Обслуживание и сервис", callback_data='c_servise')
    tele_sales_b = InlineKeyboardButton(
        "Телефонные продажи B2B", callback_data='c_tele_sales_b')
    tele_sales_c = InlineKeyboardButton(
        "Телефонные продажи B2C", callback_data='c_tele_sales_c')
    direct_sales_b = InlineKeyboardButton(
        "Прямые продажи B2B", callback_data='c_direct_sales_b')
    direct_sales_c = InlineKeyboardButton(
        "Прямые продажи B2C", callback_data='c_direct_sales_c')
    form_accept = InlineKeyboardButton(
        "Отправить!", callback_data='c_form_accept')
    experience.add(servise, tele_sales_b, tele_sales_c,
                   direct_sales_b, direct_sales_c, form_accept)

    return experience


def clear_state() -> InlineKeyboardMarkup:
    experience = ReplyKeyboardMarkup(resize_keyboard=True)
    kb = KeyboardButton("Начать сначала")
    experience.add(kb)

    return experience


experience = InlineKeyboardMarkup(row_width=1)
servise = InlineKeyboardButton(
    "Обслуживание и сервис", callback_data='c_servise')
tele_sales_b = InlineKeyboardButton(
    "Телефонные продажи B2B", callback_data='c_tele_sales_b')
tele_sales_c = InlineKeyboardButton(
    "Телефонные продажи B2C", callback_data='c_tele_sales_c')
direct_sales_b = InlineKeyboardButton(
    "Прямые продажи B2B", callback_data='c_direct_sales_b')
direct_sales_c = InlineKeyboardButton(
    "Прямые продажи B2C", callback_data='c_direct_sales_c')
form_accept = InlineKeyboardButton(
    "Отправить!", callback_data='c_form_accept')
experience.add(servise, tele_sales_b, tele_sales_c,
               direct_sales_b, direct_sales_c, form_accept)
