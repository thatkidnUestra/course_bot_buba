from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from django.contrib.sites import requests

from keyboards.inline.back_kb import back
from keyboards.inline.edit_self_keyboard import edit_kb
from loader import dp
from states.get_info import GetInfo
from utils.db_api.db_commands import get_user, update_name


@dp.callback_query_handler(Text(equals='go_edit'))
async def go_edit(call: types.CallbackQuery):
    data = await get_user(telegram_id=call.from_user.id)
    name = data.name
    nickname = data.nickname
    age = data.age

    await call.message.edit_text('📘 Ниже ты можешь увидеть свои данные:\n'
                                 f'▫️ Имя: {"Неизвестно" if name is None else name}\n'
                                 f'▫️ Никнейм: {"Неизвестно" if nickname is None else nickname}\n'
                                 f'▫️ Возраст: {"Неизвестно" if age is None else age}\n\n'
                                 f'👇 Под сообщением находится кнопка, по которой ты сможешь изменить всё это', reply_markup=edit_kb)


@dp.message_handler(text='📝 Изменить личную информацию')
async def edit_btn(message: types.Message):
    await message.delete()

    await dp.bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id - 1
    )
    data = await get_user(telegram_id=message.from_user.id)
    name = data.name
    nickname = data.nickname
    age = data.age

    await message.answer('📘 Ниже ты можешь увидеть свои данные:\n'
                         f'▫️ Имя: {"Неизвестно" if name is None else name}\n'
                         f'▫️ Никнейм: {"Неизвестно" if nickname is None else nickname}\n'
                         f'▫️ Возраст: {"Неизвестно" if age is None else age}\n\n'
                         f'👇 Под сообщением находится кнопка, по которой ты сможешь изменить всё это', reply_markup=edit_kb)


@dp.callback_query_handler(Text(equals='edit_name'))
async def edit_user_name(call: types.CallbackQuery):
    await call.message.edit_text('🔷 Введите ваше новое имя')
    await GetInfo.name.set()


@dp.message_handler(state=GetInfo.name)
async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    await update_name(telegram_id=message.from_user.id,
                      name=name)
    await message.delete()

    await dp.bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id - 1
    )

    await message.answer(f'✅ Имя успешно изменено на {name}', reply_markup=back)
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

    await message.answer(f'✅ Никнейм успешно изменён на {nickname}', reply_markup=back)
    await state.reset_state(True)


@dp.callback_query_handler(Text(equals='edit_age'))
async def edit_user_age(call: types.CallbackQuery):
    await call.message.edit_text('Введите ваш возраст (только число)')
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

        await message.answer(f'Теперь ваш возраст - {age}', reply_markup=back)
        await state.reset_state(True)

    else:
        await message.answer('Мне требуется только ЧИСЛО, соответствующее вашему возрасту, ничего более')
