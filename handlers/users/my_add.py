from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.inline.choose_game_kb import game_kb
from keyboards.inline.edit_add import edit_kb_add
from keyboards.inline.edit_self_keyboard import edit_kb
from keyboards.inline.no_add_my import no_kb, edit_my_add
from loader import dp
from utils.db_api.db_commands import get_info_row, get_user_info


@dp.message_handler(text='🧑‍💻 Моё объявление')
async def get_my_add(message: types.Message):
    add = await get_info_row(message.from_user.id)
    if add is not None:
        await message.answer('Ваше объявление:\n\n'
                             f'{add.name} ({add.nickname}), {add.age} лет, {add.game}\n\n'
                             f'{add.description}\n\n'
                             f'Выберите на клавиатуре ниже, что вы хотите изменить:', reply_markup=edit_kb_add)
    else:
        await message.answer('У вас нет своего объявления :(', reply_markup=no_kb)


@dp.callback_query_handler(Text(equals='new_add_my'))
async def new_add_my(call: types.CallbackQuery):
    '''Добавить проверку на наличие инфы о человеке'''

    data = await get_user_info(call.from_user.id)

    if data:
        await call.message.edit_text('❌ У тебя не заполнена личная информация.\n', reply_markup=edit_kb)
    else:
        add = await get_info_row(call.from_user.id)

        if add is not None:
            await call.message.edit_text('Ваше объявление:\n\n'
                                         f'{add.name} ({add.nickname}), {add.age} лет, {add.game}\n\n'
                                         f'{add.description}\n\n'
                                         f'Выберите то, что хотите изменить:', reply_markup=edit_kb_add)
        else:
            keyboard = await game_kb()

            await call.message.edit_text('Выбери игру из списка ниже:', reply_markup=keyboard)


'''НАПИСАТЬ КНОПКУ ДЛЯ СОЗДАНИЯ ОБЪЯВЛЕНИЯ'''
