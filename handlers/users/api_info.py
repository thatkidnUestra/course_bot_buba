from aiogram import types

from loader import dp

'''
Первым делом, импортируем диспатчер (dp)
При помощи него мы будем отлавливать события (апдейты) прямо из тг

В скобках указываем необязательные фильтры

'''


@dp.message_handler(text='/info')  # Реагируем на команду /info
async def info_cmd(message: types.Message):
    '''

    После того, как мы написали обработчик, пишем асинхронную функцию.


    Внегласный свод правил по написанию функций:

    - Если команда, то мы пишем название функции в виде <команда>_cmd
    пример выше

    - Если обработчик заточен под клавитуру, то аналогично с командой,
    но вместо _cmd используем _kb


    Касательно скобок, если у нас команда, то в функцию будет попадать объект Message,
    у которого есть свои параметры, которыми мы можем пользоваться

    '''

    first_name = message.from_user.first_name  # Запрашиваем из Апдейта Имя
    last_name = message.from_user.last_name  # Запрашиваем Фамилию
    username = message.from_user.username  # Запрашиваем username
    telegram_id = message.from_user.id  # Запрашиваем Telegram ID

    chat_id = message.chat.id

    await message.answer('Информация из Update:\n'
                         f'Имя: {first_name}\n'
                         f'Фамилия: {last_name}\n'
                         f'Юзернейм: {username}\n'
                         f'Telegram ID: {telegram_id}\n'
                         f'ID CHAT: {chat_id}')  # Простая отправка сообщения, где нужен только текст

    '''
    \n - перенос на след. строку
    '''

    await dp.bot.send_message(
        chat_id=449630996,
        text='Информация из Update:\n'
             f'Имя: {first_name}\n'
             f'Фамилия: {last_name}\n'
             f'Юзернейм: {username}\n'
             f'Telegram ID: {telegram_id}'
    )  # Сложная отправка сообщения
