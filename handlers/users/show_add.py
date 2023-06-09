from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.pagination_keyboard import pagination_kb
from keyboards.inline.second_action import action_kb
from loader import dp
from utils.db_api.db_commands import get_all_adds, get_info_row, get_user


@dp.message_handler(text='👀 Смотреть объявления')
async def show_add_kb(message: types.Message):
    data = await get_all_adds()
    print(len(data))

    list_id = 0

    owner_id = data[list_id].owner
    name = data[list_id].name
    nickname = data[list_id].nickname
    age = data[list_id].age
    description = data[list_id].description
    game = data[list_id].game

    keyboard = await pagination_kb(
        list_id=list_id,
        telegram_id=owner_id
    )

    await message.answer('Смотри, что я для тебя нашел:\n\n'
                         f'{name} ({nickname}), {age} лет, {game}\n\n'
                         f'{description}\n\n',
                         reply_markup=keyboard
                         )


@dp.callback_query_handler(Text(startswith='go_next_'))
async def go_next(call: types.CallbackQuery):
    list_id = int(call.data.split('_')[2])
    print(list_id)

    data = await get_all_adds()
    print(len(data))

    if list_id >= len(data):
        await call.answer('Анкеты закончились, подбор начался сначала.', show_alert=True)
        list_id = 0

    owner_id = data[list_id].owner
    name = data[list_id].name
    nickname = data[list_id].nickname
    age = data[list_id].age
    description = data[list_id].description
    game = data[list_id].game

    keyboard = await pagination_kb(
        list_id=list_id,
        telegram_id=owner_id
    )

    await call.message.edit_text('Смотри, что я для тебя нашел:\n\n'
                                 f'{name} ({nickname}), {age} лет, {game}\n\n'
                                 f'{description}\n\n',
                                 reply_markup=keyboard
                                 )

@dp.callback_query_handler(Text(startswith='go_prev_'))
async def go_next(call: types.CallbackQuery):
    list_id = int(call.data.split('_')[2])
    print(list_id)

    data = await get_all_adds()
    print(len(data))

    if list_id <= len(data):
        await call.answer('Анкеты закончились, подбор начался сначала.', show_alert=True)
        list_id = 0

    owner_id = data[list_id].owner
    name = data[list_id].name
    nickname = data[list_id].nickname
    age = data[list_id].age
    description = data[list_id].description
    game = data[list_id].game

    keyboard = await pagination_kb(
        list_id=list_id,
        telegram_id=owner_id
    )

    await call.message.edit_text('Смотри, что я для тебя нашел:\n\n'
                                 f'{name} ({nickname}), {age} лет, {game}\n\n'
                                 f'{description}\n\n',
                                 reply_markup=keyboard
                                 )
