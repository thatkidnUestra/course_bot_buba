from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def game_kb():
    keyboard = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Dota 2', callback_data='game_1')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Counter-Strike: Global Offensive', callback_data='game_2')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Minecraft', callback_data='game_3')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Fortnite', callback_data='game_4')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Roblox', callback_data='game_5')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Dead by Daylight', callback_data='game_6')
                                        ]
                                    ])

    return keyboard