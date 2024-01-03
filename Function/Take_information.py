import requests
from bs4 import BeautifulSoup
from config import headers


def get_information_about_day(city, days: list) -> list:
    days_spis = []

    for day in days:
        r = requests.get(f'https://pogoda1.ru/{city}/{day}', headers=headers)

        src = r.text

        soup = BeautifulSoup(src, 'lxml')

        weather_at_day = soup.find(class_='row-forecast-day-times').find_all(class_='row-forecast-time-of-day')

        for times_of_day in weather_at_day:
            b = day.split('-')

            day_number, month_number, year_number = b[0], b[1], b[2]
            times_of = times_of_day.find('div', class_='cell-forecast-time').text
            try:
                wind_speed = times_of_day.find(class_='cell-forecast-wind').text.strip()[:-4]
                wind_direction = times_of_day.find(class_='wind').find('img').get('alt')
            except:
                wind_direction = times_of_day.find(class_='wind').text
                wind_speed = 0

            pressure = times_of_day.find(class_='cell-forecast-press').text
            humidity = times_of_day.find(class_='cell-forecast-hum').text[:-1]
            prec = times_of_day.find(class_='cell-forecast-prec').text

            spis_param = [year_number, month_number, day_number, times_of, wind_speed, wind_direction, pressure, humidity, prec]

            days_spis.append(spis_param)

    return days_spis