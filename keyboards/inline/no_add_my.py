from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

no_kb = InlineKeyboardMarkup(row_width=3,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='Создать объявление', callback_data='new_add_my')
                                 ]
                             ])

edit_my_add = InlineKeyboardMarkup(row_width=3,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(text='Игра', callback_data='edit_game')
                                       ],
                                       [
                                           InlineKeyboardButton(text='Описание', callback_data='edit_desc')
                                       ]
                                   ])
