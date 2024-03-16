import requests
from bs4 import BeautifulSoup
import csv
from config import headers
from Function.for_day import get_information_about_day
import json
from datetime import *


def generate_date_list(start: str, end: str):
    start = datetime.strptime(start, '%d-%m-%y')
    end = datetime.strptime(end, '%d-%m-%y')
    num_days = (end - start).days
    return set([(start + timedelta(days=i)).strftime('%B-%Y').lower() for i in range(num_days)])


with open('C:\П\Yandexparser\City/Noname/Peterburg.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]

dni = sorted(list(generate_date_list('1-1-18', '3-3-24')))


csv_headers = ['Населённый пункт', 'Год', 'Месяц', 'День', 'Время_суток', 'Температура', 'Скорость_ветра(м/с)',
                       'Направление_ветра',
                       'Давление', 'Влажность', 'Осадки_(м/м)', 'Погода']


for city in lines[1:]:
    writer.writerow(csv_headers)
    for month_and_year in dni:
        with open(f'C:\П\Tg_weather_bot\Saint-Petersburg/{city[1:-1]}.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            url = f'https://pogoda1.ru{city}{month_and_year}'
            print(url)
            r = requests.get(url, headers=headers)
            src = r.text
            soup = BeautifulSoup(src, 'lxml')

            try:
                table = soup.find(class_='calendar-table').find_all(class_='calendar-item')
                for all_day in table:
                    if all_day.get('href'):
                        href = all_day.get('href')
                        day_info = get_information_about_day(f'https://pogoda1.ru/{href}')

                        if day_info is None:
                            continue
                        else:
                            for time_of_day, day_data in day_info[1].items():
                                row = [city[1:-1], int(month_and_year[-4:]), month_and_year[:-5], day_info[0], time_of_day, *day_data]
                                print(f'Запись {city[1:-1]} за {day_info[0]} {month_and_year[:-5]} {month_and_year[-4:]}....')

                                writer.writerow(row)


            except Exception:
                print('Какая-то ошибка!')
                continue

        # headers = ['Населённый пункт', 'Год', 'Месяц',
        #            'Давление', 'Влажность', 'Осадки_(м/м)', 'Погода'] 'День', 'Время_суток', 'Температура', 'Скорость_ветра(м/с)',
        #            'Направление_ветра',


        # csv_headers = ['Населённый пункт', 'Год', 'Месяц', 'День', 'Время_суток', 'Температура', 'Скорость_ветра(м/с)',
        #                'Направление_ветра',
        #                'Давление', 'Влажность', 'Осадки_(м/м)', 'Погода']
        #
        # with open(f'C:\П\Tg_weather_bot\Saint-Petersburg/{city[1:-1]}.csv', 'a', newline='', encoding='utf-8') as file:
        #     writer = csv.writer(file)
        #     writer.writerow(
        #         csv_headers)
        #
        #     for city, years in all_the_time_dict.items():
        #         for year, months in years.items():
        #             for month, days in months.items():
        #                 for day, day_data in days.items():
        #                     for time_of_day, data in day_data.items():
        #                         row = [city[1:-1], year, month, day, time_of_day] + data
        #
        #                         print(f'Запись {city[1:-1]} за {day} {month} {year}....')
        #
        #                         writer.writerow(row)
