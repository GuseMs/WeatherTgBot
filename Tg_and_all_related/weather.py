from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext, filters
from datetime import datetime

from Function.prediction_temperature import prediction_temperature
from Function.Tg_Keyboard import create_reply_keyboard, create_inline, create_double_level_inline
from Function.Take_information import get_information_about_day
from Function.Generate_date_list import generate_date_list
from Function.Pretty_message import pretty_message
from config import city_dict, ADMINS
from loder import dp, bot
from tg_bot import WeatherWait


@dp.message_handler(commands='weather')
async def inline_weather_city(message: Message):
    spis = []
    for city in city_dict.items():
        spis.append(city[0].capitalize())

    keyboard = create_reply_keyboard(*spis)
    keyboard.one_time_keyboard = True

    await message.answer(f'Выберите город:', reply_markup=keyboard)
    await WeatherWait.waiting_city_name.set()


@dp.message_handler(state=WeatherWait.waiting_city_name)
async def day_count(message: Message, state: FSMContext):
    try:
        if city_dict[str(message.text).lower()]:
            await state.update_data(city=message.text, username=message.from_user.username)

            spis = ['Сегодня', 'Завтра', '3 дня', 'Неделя', '2 недели']
            await message.answer('Выберите:', reply_markup=create_double_level_inline(spis, 'day_count'))
            await WeatherWait.next()

    except KeyError:
        await message.answer('Некорректно введено название :(\nПожалуйста, проверьте название и напишите заново:')


@dp.callback_query_handler(filters.Text(startswith='day_count_'), state=WeatherWait.waiting_day_count)
async def temperature_for_selected_days(call: CallbackQuery, state: FSMContext):
        await call.message.delete()
        text = call.data.split('_')[2]
        data = await state.get_data()
        city_name = str(data.get('city')).lower()
        username = str(data.get('username'))

        try:
            if text == 'Сегодня':
                which_days = generate_date_list(datetime.now().strftime('%d-%m-%Y'), 1)

            elif text == 'Завтра':
                which_days = generate_date_list(datetime.now().strftime('%d-%m-%Y'), 2)
                del which_days[0]

            elif text == '3 дня':
                which_days = generate_date_list(datetime.now().strftime('%d-%m-%Y'), 3)

            elif text == 'Неделя':
                which_days = generate_date_list(datetime.now().strftime('%d-%m-%Y'), 7)

            elif text == '2 недели':
                which_days = generate_date_list(datetime.now().strftime('%d-%m-%Y'), 14)

            else:
                await call.message.answer(f'Произошла ошибка\nПожалуйста, попробуйте ещё раз или обратитесь к администратору через настройки')
                await state.finish()

            day_info = get_information_about_day(f'{city_dict[city_name]}', which_days)
            print(city_dict[city_name])

            print(day_info)
            temperature = prediction_temperature(city_name, day_info)

            parse_message = pretty_message(temperature, day_info)

            for message in parse_message:
                await call.message.answer('\n'.join(*message))

            await state.finish()

        except Exception as error:
            await call.message.answer('Произошла ошибка, попробуйте ещё раз \n{если ошибка остаётся, обратитесь в поддержку нажав "Обратиться"}')

            await bot.send_message(ADMINS[0], f'Ошибка у @{username}\n\n{error}')

            await state.finish()
