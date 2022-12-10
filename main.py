from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from data_writer import add_items


storage = MemoryStorage()
bot = Bot(TOKEN_API, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage,)


users = {}


async def on_startup(_):

    print("Бот запущен")


async def on_shutdown(_):
    print("Бот остановлен")


if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )
