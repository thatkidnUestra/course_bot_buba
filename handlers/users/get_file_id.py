from aiogram import types

from loader import dp


@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def get_file_id(message: types.Message):
    file_id = message.voice.file_id
    await message.answer(file_id)
