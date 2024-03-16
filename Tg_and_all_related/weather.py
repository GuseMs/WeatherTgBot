from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.filters import Command
from Function.prediction_temperature import prediction_temperature
from Function.minor_features import *
from Function.take_information import get_information_about_day
from config import city_dict, ADMINS
from state_class import WeatherWait
from loader import bot

weather = Router()


@weather.message(Command('weather'))
async def inline_weather_city(message: Message, state: FSMContext):
    spis = []
    for city in city_dict.items():
        spis.append(city[0].capitalize())

    keyboard = create_reply_keyboard(*spis).adjust(1).as_markup()
    keyboard.one_time_keyboard = True

    await message.answer(f'Выберите город:', reply_markup=keyboard)
    await state.set_state(WeatherWait.waiting_city_name.state)


@weather.message(WeatherWait.waiting_city_name)
async def day_count(message: Message, state: FSMContext):
    try:
        if city_dict[str(message.text).lower()]:
            await state.update_data(city=message.text, username=message.from_user.username)

            spis = ['Сегодня', 'Завтра', '3 дня', 'Неделя', '2 недели']
            await message.answer('Выберите:', reply_markup=create_double_level_inline(spis, 'day_count').adjust(1).as_markup())
            await state.set_state(WeatherWait.waiting_day_count)

    except KeyError:
        await message.answer('Некорректно введено название :(\nПожалуйста, проверьте название и напишите заново:')


@weather.callback_query(WeatherWait.waiting_day_count, F.data.startswith('day_count_'))
async def temperature_for_selected_days(call: CallbackQuery, state: FSMContext):
        await call.message.delete()
        text = call.data.split('_')[2]
        data = await state.get_data()
        city_name = str(data.get('city')).lower()
        username = str(data.get('username'))
        some_dict = {'Сегодня': 1, 'Завтра': 2, '3 дня': 3, 'Неделя': 7, '2 недели': 14}
        which_days = generate_date_list(some_dict.get(text))

        try:
            if which_days is not None:
                day_info = get_information_about_day(f'{city_dict[city_name]}', which_days)

                temperature = prediction_temperature(city_dict[city_name], day_info)

                parse_message = pretty_message(temperature, day_info)

                for message in parse_message:
                    await call.message.answer('\n'.join(*message))

                await state.clear()

            else:

                await call.message.answer(
                    f'Произошла ошибка\nПожалуйста, попробуйте ещё раз или обратитесь к администратору через настройки')
                await state.clear()

        except Exception as error:
            await call.message.answer('Произошла ошибка, попробуйте ещё раз \n{если ошибка остаётся, обратитесь в поддержку, нажав "Обратиться", в настройках}')

            await bot.send_message(ADMINS[0], f'Ошибка у @{username}\n\n{error}')

            await state.clear()