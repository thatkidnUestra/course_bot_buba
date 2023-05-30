from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.pagination_keyboard import pagination_kb
from keyboards.inline.second_action import action_kb
from loader import dp
from utils.db_api.db_commands import get_all_adds, get_info_row, get_user


@dp.callback_query_handler(Text(startswith='send_'))
async def send_invite(call: types.CallbackQuery):
    telegram_id = call.data.split('_')[1]

    user_add = await get_info_row(telegram_id)

    keyboard = await action_kb(call.from_user.id)

    await dp.bot.send_message(
        chat_id=telegram_id,
        text='Кто-то тобой заинтересовался.\n\n'
             f'{user_add.name} ({user_add.nickname}), {user_add.age} лет, {user_add.game}\n\n'
             f'{user_add.description}\n\n'
             f'Выбери действие на клавиатуре ниже:',
        reply_markup=keyboard
    )

    await call.answer('Твое приглашение отправлено!', show_alert=True)


@dp.callback_query_handler(Text(startswith='accept_'))
async def accept_invite(call: types.CallbackQuery):
    telegram_id_second = call.data.split('_')[1]

    await dp.bot.send_message(
        chat_id=telegram_id_second,
        text=f'@{call.from_user.username} согласился быть напарником\n'
             f'Напиши ему!'
    )

    await call.message.edit_text('Супер! Удачных каток!\n'
                                 f'Твой тиммейт скоро напишет тебе')


@dp.callback_query_handler(Text(startswith='no_'))
async def no_invite(call: types.CallbackQuery):
    await call.message.edit_text('Вы успешно отказались!')
