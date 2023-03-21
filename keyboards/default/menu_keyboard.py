from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text='Показать номер', request_contact=True),
        KeyboardButton(text='Показать меню')
    ],
    [
        KeyboardButton(text='Показать локацию', request_location=True)
    ],
    [
        KeyboardButton(text='Буба')
    ]
])
