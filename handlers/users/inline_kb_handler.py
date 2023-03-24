from aiogram import types
from aiogram.dispatcher.filters import Text

from handlers.users.default_kb_handler import just_button_reaction
from keyboards.inline.second_menu import inline_menu, inline_back
from loader import dp
import random


@dp.callback_query_handler(Text(equals='go_back'))
async def go_back(call: types.CallbackQuery):
    await call.message.delete()
    await just_button_reaction(message=call.message)

    '''
    await just_button_reaction(message=call.message) <- Это мы вызвали функцию для отправки сообщения с изначальной клавиатурой
    '''


@dp.callback_query_handler(Text(equals='get_number'))
async def get_random_number(call: types.CallbackQuery):
    number = random.randint(0, 10000)

    """
        await call.answer('хеех', show_alert=True) <- Это уведомление на весь экран
        await call.message.answer(f'Вот ваше число: {number}') <- Это для ОТПРАВКИ сообщения
    """

    await call.message.edit_text(f'Вот ваше число: {number}', reply_markup=inline_back)


@dp.callback_query_handler(Text(equals='show_meme'))
async def get_super_meme(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        photo='https://i.ytimg.com/vi/a31-_ivqtRM/maxresdefault.jpg',
        caption='лови!',
        reply_markup=inline_back
    )


@dp.callback_query_handler(Text(equals='ur_soul_is_mine'))
async def run_away(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer('а теперь..', show_alert=True)
    await call.message.answer_photo(
        photo='https://www.meme-arsenal.com/memes/10b4258a21dd26c4c7c5218e1e0ec040.jpg',
        caption='...',
        reply_markup=inline_back
    )
    file_id = 'AwACAgIAAxkBAAICoGQd1r2KVCihqz055ILt1Tk5n7B-AALhJwACMjvxSCYrg0uspxLGLwQ'
    await call.message.answer_voice(
        voice=file_id
    )

'''
await call.message.delete()
await call.message.answer_photo(
photo=ссылка на фото,
caption='Вот этот мем))))'
)
'''

'''
    file_id = 'AwACAgIAAxkBAAICj2QZyx-mb0qfKgAB-51GUmSxJLbJ3gAC0CkAAj5L0EhR39UoK_CaJC8E'
    await call.message.answer_voice(
        voice=file_id
    )
    


'''