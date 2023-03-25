from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

edit_kb = InlineKeyboardMarkup(row_width=3,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='🔹 Изменить имя', callback_data='edit_name')
                                   ],
                                   [
                                       InlineKeyboardButton(text='🔹 Изменить никнейм', callback_data='edit_nickname')
                                   ],
                                   [
                                       InlineKeyboardButton(text='🔹 Изменить возраст', callback_data='edit_age')
                                   ],
                                   [
                                       InlineKeyboardButton(text='<< Назад', callback_data='go_menu')
                                   ]
                               ])
