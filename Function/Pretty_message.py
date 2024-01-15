import pandas as pd
from config import code_to_smile

def pretty_message(result_dict: dict, day_info: list) -> list:
    message_with_temperature = []
    chet = 0
    for date, time_temperature_list in result_dict.items():
        formatted_date = pd.to_datetime(date, format="%d.%m.%Y").strftime("%d %B")
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