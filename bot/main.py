import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.default import keyboard_def
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import sqlite3
from states import CallbackStates

# ----------#

from aiogram.types import CallbackQuery

connect = sqlite3.connect('../db.sqlite3', check_same_thread=False)
cursor = connect.cursor()

API_TOKEN = '7035105679:AAHcWXjb97wm2DyH8le5juzsHNT2G9hGHu4'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.callback_query_handler(commands=['start'])
async def process_start_command(call: types.CallbackQuery):
    await call.message.answer("Start", reply_markup=keyboard_def)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


