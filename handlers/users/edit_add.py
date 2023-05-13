from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline.choose_game_kb import get_edit_game_kb
from loader import dp
from states.get_info import GetInfo
from utils.db_api.db_commands import get_game_by_id, update_game, update_desc


@dp.callback_query_handler(Text(equals='edit_game'))
async def edit_user_game(call: types.CallbackQuery):
    keyboard = await get_edit_game_kb()

    await call.message.edit_text('Выбери игру из списка ниже:', reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith='egame_'))
async def get_edit_game(call: types.CallbackQuery):
    data = int(call.data.split('_')[1])
    game = await get_game_by_id(data)
    await update_game(
        owner_id=call.from_user.id,
        game=game.name
    )
    await call.message.edit_text(f'Вы успешно изменили игру на {game.name}')


@dp.callback_query_handler(Text(equals='edit_desc'))
async def go_edit_desc(call: types.CallbackQuery):
    await call.message.edit_text('Напиши мне новое описание твоего объявления.')
    await GetInfo.edit_desc.set()


@dp.message_handler(state=GetInfo.edit_desc)
async def get_edited_desc(message: types.Message, state: FSMContext):
    await state.reset_state(True)
    desc = message.text
    await update_desc(
        owner_id=message.from_user.id,
        desсription=desc
    )
    await message.answer('Вы успешно изменили описание на:\n\n'
                         f'{desc}')
