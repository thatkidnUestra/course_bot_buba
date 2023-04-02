from aiogram.dispatcher.filters.state import StatesGroup, State


class GetInfo(StatesGroup):
    name = State()
    nickname = State()
    age = State()

    description = State()
