from aiogram import executor, types, Dispatcher
from loder import dp

from Function.prediction_temperature import prediction_temperature
from Function.For_day import get_information_about_day

import logging
from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import city_dict


logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def hello(message: types.Message):
    await message.answer(f'''Привет, {message.from_user.first_name}!\n'''
                         '''С помощью этого бота можно узнать погоду в любом городе России{скоро}!\n'''
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


class WeatherWait(StatesGroup):
    waiting_city_name = State()
    waiting_day_count = State()


@dp.message_handler(commands='weather')
async def inline_weather_city(message: types.Message):
    await message.answer(f'Введите название города:')
    await WeatherWait.waiting_city_name.set()


@dp.message_handler(state=WeatherWait.waiting_city_name)
async def day_count(message: types.Message, state: FSMContext):
    try:
        if city_dict[str(message.text).lower()]:
            await state.update_data(city=message.text)

            markup = types.InlineKeyboardMarkup()
            for day in ['Сегодня', 'Завтра', '3 дня', 'Неделя', '2 недели']:
                markup.insert(types.InlineKeyboardButton(day, callback_data='day_count'))

            await message.answer('Выберите:', reply_markup=markup)
            await WeatherWait.next()

    except KeyError:
        await message.answer('Некорректно введено название :(\nПожалуйста, проверьте название и напишите заново:')


@dp.callback_query_handler(state=WeatherWait.waiting_day_count, text='day_count')
async def temperature_for_today(call: types.CallbackQuery, state: FSMContext):
        await call.message.delete()
        data = await state.get_data()
        city_name = str(data.get('city')).lower()
        day_info = get_information_about_day(f'https://pogoda1.ru/{city_dict[city_name]}')

        date = day_info[0]
        weather_data = day_info[1]
        year = datetime.now().strftime('%Y')
        month = datetime.now().strftime('%B').lower()

        result_list = []

        for time_of_day, values in weather_data.items():
            current_list = [city_name, year, month, date, time_of_day]
            current_list.extend(values)
            result_list.append(current_list)

        result_tuple = tuple(result_list)

        temperatures = prediction_temperature(result_tuple)

        await call.message.answer(f'Температура сейчас: {temperatures[0]}℃')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)