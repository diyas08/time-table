from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_def = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Расписание классов')
        ],
        [
            KeyboardButton(text='Расписание учителей')
        ],
    ], resize_keyboard=True
)