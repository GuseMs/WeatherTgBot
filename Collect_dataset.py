import requests
from bs4 import BeautifulSoup
import csv
from config import headers
from Function.For_day import get_information_about_day
import json

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
          'december']
years = ['2018', '2019', '2020', '2021', '2022', '2023']

all_the_time_dict = {}

for year in years:

    year_dict = {}

    for month in months:
        month_dict = {}
        url = f'https://pogoda1.ru/sarov/{month}-{year}'

        r = requests.get(url, headers=headers)
        src = r.text
        soup = BeautifulSoup(src, 'lxml')

        try:
            table = soup.find(class_='calendar-table').find_all(class_='calendar-item')
            for all_day in table:
                if all_day.get('href'):
                    href = all_day.get('href')
                    day_info = get_information_about_day(f'https://pogoda1.ru/{href}')
                    month_dict[day_info[0]] = day_info[1]

        except Exception:
            continue

        year_dict[month] = month_dict

    all_the_time_dict[year] = year_dict

with open('City/Sarov.scv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    headers = ['Год', 'Месяц', 'День', 'Время_суток', 'Температура', 'Скорость_ветра(м/с)', 'Направление_ветра',
               'Давление', 'Влажность', 'Осадки_(м/м)']
    writer.writerow(headers)

    for year, months in all_the_time_dict.items():
        for month, days in months.items():
            for day, day_data in days.items():
                for time_of_day, data in day_data.items():
                    row = [year, month, day, time_of_day] + data
                    writer.writerow(row)