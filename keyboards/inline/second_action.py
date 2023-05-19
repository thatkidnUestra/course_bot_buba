from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def action_kb(telegram_id_second):
    keyboard = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Согласиться', callback_data=f'accept_{telegram_id_second}'),
                                            InlineKeyboardButton(text='Отказаться', callback_data=f'no_{telegram_id_second}')
                                        ]
                                    ])
    return keyboard
