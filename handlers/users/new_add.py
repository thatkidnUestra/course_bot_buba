from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline.choose_game_kb import game_kb, get_edit_game_kb
from keyboards.inline.edit_add import edit_kb_add
from keyboards.inline.edit_self_keyboard import edit_kb
from loader import dp
from states.get_info import GetInfo
from utils.db_api.db_commands import get_user_info, get_game_by_id, get_user, create_row_adds, get_info_row, update_game


@dp.message_handler(text='📩 Новое объявление')
async def new_add_user(message: types.Message):
    '''Добавить проверку на наличие инфы о человеке'''

    data = await get_user_info(message.from_user.id)

    if data:
        await message.answer('❌ У тебя не заполнена личная информация.\n', reply_markup=edit_kb)
    else:
        add = await get_info_row(message.from_user.id)

        if add is not None:
            await message.answer('Ваше объявление:\n\n'
                                 f'{add.name} ({add.nickname}), {add.age} лет, {add.game}\n\n'
                                 f'{add.description}\n\n'
                                 f'Выберите то, что хотите изменить:', reply_markup=edit_kb_add)
        else:
            keyboard = await game_kb()
            await message.delete()

            await message.answer('Выбери игру из списка ниже:', reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith='game_'))
async def get_game(call: types.CallbackQuery):
    data = int(call.data.split('_')[1])
    game_name = await get_game_by_id(data)
    await GetInfo.description.set()

    state = dp.current_state(
        chat=call.message.chat.id,
        user=call.from_user.id
    )

    await state.update_data(
        {
            'game': game_name.name
        }
    )

    await call.message.answer('Теперь напиши описание к своему объявлению\n'
                              '(<i>это может быть что угодно, к примеру, режим игры, твои требования к потенциальному тиммейту и т.д.</i>)')


@dp.message_handler(state=GetInfo.description)
async def get_description(message: types.Message, state: FSMContext):
    '''Так же сделать подвязку к личной информации, дабы отобразить объявление перед публикацией'''
    description = message.text

    data = await state.get_data()

    user_data = await get_user(message.from_user.id)

    game = data.get('game')

    await message.answer('Теперь твоё объявление выглядит так:\n\n'
                         f'{user_data.name} ({user_data.nickname}), {user_data.age} лет, {game}\n\n'
                         f'{description}')

    await create_row_adds(
        owner_id=message.from_user.id,
        name=user_data.name,
        nickname=user_data.nickname,
        age=user_data.age,
        description=description,
        game=game
    )

    await state.reset_state(True)


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
