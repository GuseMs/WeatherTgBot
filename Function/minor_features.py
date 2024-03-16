import re
import pandas as pd
from config import code_to_smile
# from loder import dp
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from localisation import cancel
from datetime import *


def extract_precipitation(s):
    match = re.search(r'(-?\d+(\.\d+)?)', s)
    return float(match.group(1)) if match else 0


def extract_temperature(temperaturestr):
    match = re.search(r'(-?\d+)', temperaturestr)
    return int(match.group(1)) if match else None


def pretty_message(result_dict: dict, day_info: list) -> list:
    message_with_temperature = []
    chet = 0
    for date, time_temperature_list in result_dict.items():
        formatted_date = pd.to_datetime(date, format="%d.%B.%Y").strftime("%d %B")
        day_temperature_data = [formatted_date]

        for day_time_dict in time_temperature_list:

            for time_of_day, temperature in day_time_dict.items():
                day_temperature_data.append(f"{time_of_day.capitalize()}: {temperature} ℃\n\t\t\t"
                                            f"Погода: {code_to_smile[day_info[chet][9]]}\n\t\t\t"
                                            f"Осадки: {day_info[chet][8]}\n\t\t\t"
                                            f'Скорость ветра: {day_info[chet][4]} м/с\n\t\t\t'
                                            f"Направление ветра: {day_info[chet][5]}"
                                            )

                chet += 1
        message_with_temperature.append([day_temperature_data])

    return message_with_temperature


def create_reply_keyboard(*buttons):
    replymarkup = ReplyKeyboardBuilder()
    for i in buttons:
        replymarkup.add(KeyboardButton(text=i))
    return replymarkup


def create_double_level_inline(buttons: list, startswith: str):
    inlinemarkup = InlineKeyboardBuilder()
    for i in buttons:
        inlinemarkup.add(InlineKeyboardButton(text=f'{i}', callback_data=f'{startswith}_{i}'))
    return inlinemarkup


def create_inline(*buttons):
    inlinemarkup = InlineKeyboardBuilder()
    for i in buttons:
        inlinemarkup.add(InlineKeyboardButton(text=f'{i}', callback_data=f'{i}'))
    return inlinemarkup


def create_inline_url(url: dict):
    inlinemarkup = InlineKeyboardBuilder()
    for i in url:
        inlinemarkup.add(InlineKeyboardButton(text=f'{i}', url=f'{url[i]}'))
    inlinemarkup.add(InlineKeyboardButton(text=f'{cancel}', callback_data=f'{cancel}'))
    return inlinemarkup


async def update_text(message: Message, new_text: str, new_inlinemarkup):
    if message.text != new_text or message.reply_markup != new_inlinemarkup:
        await message.edit_text(new_text, reply_markup=new_inlinemarkup)


def generate_date_list(num_days: int): return \
    [(datetime.strptime(datetime.now().strftime('%d-%m-%Y'), '%d-%m-%Y') + timedelta(days=i)).strftime('%d-%m-%Y') for i in range(num_days)]