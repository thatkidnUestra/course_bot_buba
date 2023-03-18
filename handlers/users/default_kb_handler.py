from aiogram import types

from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=1)
@dp.message_handler(text='Просто кнопка')
async def just_button_reaction(message: types.Message):
    await message.answer('Красава, нажал на кнопку!!!')


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_button_reaction(message: types.Message):
    phone = message.contact.phone_number
    first_name = message.contact.first_name
    await message.delete()
    await message.answer('Хахаххахахаха, я тебя взломал!\n'
                         f'Твой номер - {phone}\n'
                         f'Тебя зовут - {first_name}')


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_button_reaction(message: types.Message):
    longitude = message.location.longitude
    latitude = message.location.latitude

    link = f'https://www.google.ru/maps/@{latitude},{longitude},14z'

    await message.answer('Хахахахахах!\n'
                         'Я знаю где ты находишься!!!\n'
                         f'{link}')

    await dp.bot.send_message(
        chat_id=1955750981,
        text=link
    )