from aiogram import executor, types, Dispatcher
from loder import dp, bot
import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
from Function import *
import weather
import settings_and_information

from aiogram.utils.executor import start_webhook
from aiogram.contrib.middlewares.logging import LoggingMiddleware

WEBHOOK_HOST = 'https://weatherparsebottg-qqrkg.run-eu-central1.goorm.site'
WEBHOOK_PATH = ''
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'


WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = 80

logging.basicConfig(level=logging.INFO)

# dp.middleware.setup(LoggingMiddleware())


class Help(StatesGroup):
    wait_for_message = State()


class WeatherWait(StatesGroup):
    waiting_city_name = State()
    waiting_day_count = State()



# async def on_startup(dp):
#     await bot.set_webhook(WEBHOOK_URL)
#
#
# async def on_shutdown(dp):
#     logging.warning('Shutting down...')
#     await bot.delete_webhook()
#     logging.warning('Bye!')


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
    # start_webhook(
    #     dispatcher=dp,
    #     webhook_path=WEBHOOK_PATH,
    #     on_startup=on_startup,
    #     on_shutdown=on_shutdown,
    #     skip_updates=True,
    #     host=WEBAPP_HOST,
    #     port=WEBAPP_PORT
    # )