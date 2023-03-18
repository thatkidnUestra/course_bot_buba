from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.default.menu_keyboard import menu
from loader import dp

@dp.message_handler(CommandStart())
async def bot_start_no_state(message: types.Message):
    await message.answer('привет!', reply_markup=menu)
