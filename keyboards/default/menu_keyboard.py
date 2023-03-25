from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text='👀 Смотреть объявления'),
    ],
    [
        KeyboardButton(text='📩 Новое объявление'),
        KeyboardButton(text='📝 Изменить "О себе"')
    ],
    [
        KeyboardButton(text='🧑‍💻 Моё объявление')
    ]
])
