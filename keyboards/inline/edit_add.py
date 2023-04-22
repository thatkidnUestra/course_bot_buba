from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

edit_kb_add = InlineKeyboardMarkup(row_width=3,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='Изменить игру', callback_data='edit_game')
                                   ],
                                   [
                                       InlineKeyboardButton(text='Изменить описание', callback_data='edit_desc')
                                   ]
                               ])
