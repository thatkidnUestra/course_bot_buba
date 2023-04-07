from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline.choose_game_kb import game_kb
from loader import dp
from states.get_info import GetInfo


@dp.message_handler(text='📩 Новое объявление')
async def new_add_user(message: types.Message):
    '''Добавить проверку на наличие инфы о человеке'''

    keyboard = await game_kb()

    await message.delete()

    await dp.bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id - 1
    )

    await message.answer('Выбери игру из списка ниже:', reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith='game_'))
async def get_game(call: types.CallbackQuery):
    data = int(call.data.split('_')[1])

    if data == 1:
        await call.message.edit_text('Твой выбор - Dota 2')

        await GetInfo.description.set()

        state = dp.current_state(
            chat=call.message.chat.id,
            user=call.from_user.id
        )

        await state.update_data(
            {
                'game': 'Dota 2'
            }
        )

    elif data == 2:
        await call.message.edit_text('Твой выбор - CS:GO')

        await GetInfo.description.set()

        state = dp.current_state(
            chat=call.message.chat.id,
            user=call.from_user.id
        )

        await state.update_data(
            {
                'game': 'CS:GO'
            }
        )

    elif data == 3:
        await call.message.edit_text('Твой выбор - Minecraft')

        await GetInfo.description.set()

        state = dp.current_state(
            chat=call.message.chat.id,
            user=call.from_user.id
        )

        await state.update_data(
            {
                'game': 'Minecraft'
            }
        )

    elif data == 4:
        await call.message.edit_text('Твой выбор - Fortnite')

        await GetInfo.description.set()

        state = dp.current_state(
            chat=call.message.chat.id,
            user=call.from_user.id
        )

        await state.update_data(
            {
                'game': 'Fortnite'
            }
        )

    elif data == 5:
        await call.message.edit_text('Твой выбор - Roblox')

        await GetInfo.description.set()

        state = dp.current_state(
            chat=call.message.chat.id,
            user=call.from_user.id
        )

        await state.update_data(
            {
                'game': 'Roblox'
            }
        )

    elif data == 6:
        await call.message.edit_text('Твой выбор - Dead by Daylight')

        await GetInfo.description.set()

        state = dp.current_state(
            chat=call.message.chat.id,
            user=call.from_user.id
        )

        await state.update_data(
            {
                'game': 'Dead by Daylight'
            }
        )
    await call.message.answer('Теперь напиши описание к своему объявлению\n'
                              '(<i>это может быть что угодно, к примеру, режим игры, твои требования к потенциальному тиммейту и т.д.</i>)')

@dp.message_handler(state=GetInfo.description)
async def get_description(message: types.Message, state: FSMContext):
    '''Так же сделать подвязку к личной информации, дабы отобразить объявление перед публикацией'''
    description = message.text

    data = await state.get_data()

    game = data.get('game')

    await message.answer('Теперь твоё объявление выглядит так:\n'
                         f'{None} ({None}), {None}, {game}\n'
                         f'{description}')

    await state.reset_state(True)
