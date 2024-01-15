import requests
from bs4 import BeautifulSoup
import csv
from config import headers
from Function.For_day import get_information_about_day
import json

with open('City/Noname/Peterburg.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
          'december']
years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024']

for city in lines:
    all_the_time_dict = {}
    city_dict = {}

    for year in years:

        year_dict = {}

        for month in months:
            month_dict = {}
            url = f'https://pogoda1.ru{city}{month}-{year}'
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

                        if day_info == None:
                            continue
                        else:
                            month_dict[day_info[0]] = day_info[1]

            except Exception:
                continue

            year_dict[month] = month_dict

        city_dict[year] = year_dict

    all_the_time_dict[city] = city_dict

    csv_headers = ['Населённый пункт', 'Год', 'Месяц', 'День', 'Время_суток', 'Температура', 'Скорость_ветра(м/с)',
                   'Направление_ветра',
                   'Давление', 'Влажность', 'Осадки_(м/м)', 'Погода']

    with open(f'C:\П\Tg_weather_bot\Saint-Petersburg/{city[1:-1]}.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            csv_headers)

        for city, years in all_the_time_dict.items():
            for year, months in years.items():
                for month, days in months.items():
                    for day, day_data in days.items():
                        for time_of_day, data in day_data.items():
                            row = [city[1:-1], year, month, day, time_of_day] + data

                            print(f'Запись {city[1:-1]} за {day} {month} {year}....')

                            writer.writerow(row)
