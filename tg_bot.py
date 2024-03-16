import logging
import asyncio
import sys
from aiogram import types, filters
from Function.minor_features import create_reply_keyboard
from Tg_and_all_related.settings_and_information import settings_and_info
from Tg_and_all_related.weather import weather
from loader import dp, bot

dp.include_routers(settings_and_info, weather) # -

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


@dp.message(filters.CommandStart())
async def hello(message: types.Message):
    await message.answer(f'''Привет, {message.from_user.first_name}!\n'''
                         '''С помощью этого бота можно узнать погоду в любом городе России{скоро}!\n'''
                         '''Введи /, чтобы увидеть список моих команд''')


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=[
        types.BotCommand(command='weather', description='Перейти к погоде'),
        types.BotCommand(command='settings', description='Настройки'),
        types.BotCommand(command='information', description='Информация о проекте')
    ])
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()) # - allowed_updates говорит нам, какие апдейты обрабатывать


if __name__ == '__main__':
    asyncio.run(main())