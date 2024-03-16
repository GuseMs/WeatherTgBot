from aiogram.fsm.state import State, StatesGroup


class Help(StatesGroup):
    wait_for_message = State()


class WeatherWait(StatesGroup):
    waiting_city_name = State()
    waiting_day_count = State()