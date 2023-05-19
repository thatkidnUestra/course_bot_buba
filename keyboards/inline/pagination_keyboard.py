from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def pagination_kb(list_id: int, telegram_id: int):
    keyboard = InlineKeyboardMarkup(row_width=3,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='<-', callback_data=f'go_prev_{list_id - 1}'),
                                            InlineKeyboardButton(text='Action', callback_data=f'send_{telegram_id}'),
                                            InlineKeyboardButton(text='->', callback_data=f'go_next_{list_id + 1}')
                                        ]
                                    ])

    return keyboard
