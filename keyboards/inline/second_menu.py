from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_menu = InlineKeyboardMarkup(row_width=3,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(text='Рандомное число', callback_data='get_number'),
                                       ],
                                       [
                                           InlineKeyboardButton(text='Показать мем', callback_data='show_meme'),
                                       ],
                                       [
                                           InlineKeyboardButton(text='Пойти на работу', callback_data='go_work'),
                                       ],
                                       [
                                           InlineKeyboardButton(text='...', callback_data='ur_soul_is_mine')
                                       ]
                                   ])

inline_back = InlineKeyboardMarkup(row_width=3,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(text='<< Назад', callback_data='go_back')
                                       ]
                                   ])