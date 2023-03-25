from aiogram import types
from aiogram.dispatcher.filters import CommandStart, Text

from keyboards.default.menu_keyboard import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start_no_state(message: types.Message):
    await message.answer(f'👋  Привет, {message.from_user.first_name}!\n'
                         f'🤖 Я бот, который поможет найти тебе тиммейта или команду\n\n'
                         f'<i> 👇Для взаимодействия со мной, пользуйся клавиатурой ниже</i>', reply_markup=menu)


@dp.callback_query_handler(Text(equals='go_menu'))
async def go_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(f'👋  Привет, {call.from_user.first_name}!\n'
                              f'🤖 Я бот, который поможет найти тебе тиммейта или команду\n\n'
                              f'<i> 👇Для взаимодействия со мной, пользуйся клавиатурой ниже</i>', reply_markup=menu)
