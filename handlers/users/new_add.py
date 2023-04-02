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
        await call.message.edit_text('Dota 2?\n\n'
                                     'Отличный выбор!\n'
                                     'Напиши мне, для какого режима и т.д. ты ищешь тимейтов.')

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


@dp.message_handler(state=GetInfo.description)
async def get_description(message: types.Message, state: FSMContext):
    '''Так же сделать подвязку к личной информации, дабы отобразить объявление перед публикацией'''
    description = message.text

    data = await state.get_data()

    game = data.get('game')

    await message.answer('Готово! Ваше объявление выглядит так:\n'
                         f'Имя: {None}\n'
                         f'Возраст: {None}\n'
                         f'Никнейм: {None}\n'
                         f'Игра: {game}\n'
                         f'Описание: {description}')

    await state.reset_state(True)
