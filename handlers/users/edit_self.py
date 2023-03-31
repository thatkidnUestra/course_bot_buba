from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline.back_kb import back
from keyboards.inline.edit_self_keyboard import edit_kb
from loader import dp
from states.get_info import GetInfo


@dp.callback_query_handler(Text(equals='go_edit'))
async def go_edit(call: types.CallbackQuery):
    name = None
    nickname = None
    age = None

    await call.message.edit_text('👌 Отлично!\n'
                                 '📘 Так выглядит текущая информация о тебе:\n'
                                 f'▫️ Имя: {name}\n'
                                 f'▫️ Никнейм: {nickname}\n'
                                 f'▫️ Возраст: {age}\n\n'
                                 f'👇 Выбери то, что необходимо изменить.', reply_markup=edit_kb)


@dp.message_handler(text='📝 Изменить "О себе"')
async def edit_btn(message: types.Message):
    await message.delete()

    await dp.bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id - 1
    )

    name = None
    nickname = None
    age = None

    await message.answer('👌 Отлично!\n'
                         '📘 Так выглядит текущая информация о тебе:\n'
                         f'▫️ Имя: {name}\n'
                         f'▫️ Никнейм: {nickname}\n'
                         f'▫️ Возраст: {age}\n\n'
                         f'👇 Выбери то, что необходимо изменить.', reply_markup=edit_kb)


@dp.callback_query_handler(Text(equals='edit_name'))
async def edit_user_name(call: types.CallbackQuery):
    await call.message.edit_text('🔷 Введите ваше новое имя')
    await GetInfo.name.set()


@dp.message_handler(state=GetInfo.name)
async def get_name(message: types.Message, state: FSMContext):
    name = message.text

    await message.delete()

    await dp.bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id - 1
    )

    await message.answer(f'✅ Теперь я знаю, что вас зовут - {name}', reply_markup=back)
    await state.reset_state(True)


@dp.callback_query_handler(Text(equals='edit_nickname'))
async def edit_user_nickname(call: types.CallbackQuery):
    await call.message.edit_text('🔷 Введите ваш новый никнейм')
    await GetInfo.nickname.set()


@dp.message_handler(state=GetInfo.nickname)
async def get_nickname(message: types.Message, state: FSMContext):
    nickname = message.text

    await message.delete()

    await dp.bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id - 1
    )

    await message.answer(f'✅ Теперь я знаю, что ваш никнейм - {nickname}', reply_markup=back)
    await state.reset_state(True)


@dp.callback_query_handler(Text(equals='edit_age'))
async def edit_user_age(call: types.CallbackQuery):
    await call.message.edit_text('Введите ваш возраст')
    await GetInfo.age.set()


@dp.message_handler(state=GetInfo.age)
async def get_age(message: types.Message, state: FSMContext):
    age = message.text

    if age.isdigit():

        await message.delete()

        await dp.bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id - 1
        )

        await message.answer(f'Теперь я знаю, что тебе {age} лет', reply_markup=back)
        await state.reset_state(True)

    else:
        await message.answer('Вы ввели не число. Попробуйте еще раз.')

