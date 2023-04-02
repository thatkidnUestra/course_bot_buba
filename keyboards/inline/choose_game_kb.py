from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def game_kb():
    keyboard = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Dota 2', callback_data='game_1')
                                        ]
                                    ])

    return keyboard
