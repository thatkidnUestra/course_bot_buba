from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.db_commands import get_games


async def game_kb():
    keyboard = InlineKeyboardMarkup(row_width=3)
    games = await get_games()

    for i in range(len(games)):
        game = games[i].name
        button = InlineKeyboardButton(text=game, callback_data=f'game_{i + 1}')
        keyboard.row(button)

    return keyboard

async def get_edit_game_kb():
    keyboard = InlineKeyboardMarkup(row_width=3)
    games = await get_games()

    for i in range(len(games)):
        game = games[i].name
        button = InlineKeyboardButton(text=game, callback_data=f'egame_{i + 1}')
        keyboard.row(button)

    return keyboard
