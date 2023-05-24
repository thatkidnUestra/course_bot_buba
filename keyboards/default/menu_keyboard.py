from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text='👀 Смотреть объявления'),
    ],
    [
        KeyboardButton(text='📩 Разместить новое объявление'),
        KeyboardButton(text='📝 Изменить личную информацию')
    ],
    [
        KeyboardButton(text='‍🧑‍💻 Моё объявление')
    ]
])
