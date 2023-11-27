import requests
from bs4 import BeautifulSoup
from config import headers


def get_information_about_day(url):
    r = requests.get(url, headers=headers)
    src = r.text
    soup = BeautifulSoup(src, 'lxml')

    day = soup.find(class_='forecast-day-name').text.split()[0]

    weather_at_day = soup.find(class_='row-forecast-day-times').find_all(class_='row-forecast-time-of-day')

    day_dict = {}

    for times_of_day in weather_at_day:

        times_of = times_of_day.find('div', class_='cell-forecast-time').text
        temp = times_of_day.find('div', class_='cell-forecast-temp').text

        try:
            wind_speed = times_of_day.find(class_='cell-forecast-wind').text.strip()[:-4]
            wind_direction = times_of_day.find(class_='wind').find('img').get('alt')
        except:
            wind_direction = times_of_day.find(class_='wind').text
            wind_speed = 0

        pressure = times_of_day.find(class_='cell-forecast-press').text
        humidity = times_of_day.find(class_='cell-forecast-hum').text[:-1]
        prec = times_of_day.find(class_='cell-forecast-prec').text
        spis_param = [temp, wind_speed, wind_direction, pressure, humidity, prec]

        day_dict[times_of] = spis_param

    return day, day_dict