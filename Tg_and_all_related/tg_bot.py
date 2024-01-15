import sys
sys.path.append('C:\П\Tg_weather_bot')


from aiogram import executor, types, Dispatcher
from loder import dp, bot
import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
from Function import *
import weather
import settings_and_information

logging.basicConfig(level=logging.INFO)


class Help(StatesGroup):
    wait_for_message = State()


class WeatherWait(StatesGroup):
    waiting_city_name = State()
    waiting_day_count = State()


@dp.message_handler(commands='start')
async def hello(message: types.Message):
    await message.answer(f'''Привет, {message.from_user.first_name}!\n'''
                         '''С помощью этого бота можно узнать погоду в любом городе России{скоро}!\n'''
                         '''Введи /, чтобы увидеть список моих команд''')
    await set_commands(message)


async def set_commands(sp: Dispatcher):
    await sp.bot.set_my_commands(
        [
        types.BotCommand('/weather', 'Перейти к погоде'),
        types.BotCommand('/settings', 'Настройки'),
        types.BotCommand('/information', 'Информация о проекте')
        ]
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
