import pandas as pd


def pretty_message(result_dict: dict) -> list:
    message_with_temperature = []

    for date, time_temperature_list in result_dict.items():
        formatted_date = pd.to_datetime(date, format="%d.%m.%Y").strftime("%d %B")
        day_temperature_data = [formatted_date]

        for day_time_dict in time_temperature_list:

            for time_of_day, temperature in day_time_dict.items():
                day_temperature_data.append(f"{time_of_day}: {temperature} ℃")

        message_with_temperature.append([day_temperature_data])

    return message_with_temperature