from aiogram import executor, types, Dispatcher
from loder import dp
import logging

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def hello(message: types.Message):
    await message.answer(f'''Привет, {message.from_user.first_name}!\n'''
                         '''С помощью этого бота можно узнать погоду в любом городе России!\n'''
                         '''веди /, чтобы увидеть список моих команд''')
    await set_commands(message)


async def set_commands(sp: Dispatcher):
    await sp.bot.set_my_commands(
        [
        types.BotCommand('/weather', 'Перейти к погоде'),
        types.BotCommand('/help', 'Создать заявку о помощи'),
        types.BotCommand('/author', 'О разработчиках'),
        ]
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)