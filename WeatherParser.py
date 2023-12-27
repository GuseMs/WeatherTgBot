import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
import os
import random
import aspose.cells
from aspose.cells import Workbook
import csv
from config import headers
# url = 'https://www.gismeteo.ru/catalog/russia/'


'''РОССИЯ И ЕЁ РЕГИОНЫ'''
# r = requests.get(url, headers=headers)
#
# src = r.text

# with open('GismeteoWeather.html', 'w', encoding='UTF-8') as file:
#     file.write(src)

# with open('GismeteoWeather.html', encoding='UTF-8') as file:
#     src = file.read()
#
#
# soup = BeautifulSoup(src, 'lxml')

# # Находим все ссылки на все регионы России
# all_region_href = soup.find(class_='two-columns').find(class_='catalog-list').find_all(class_='catalog-item-link')
#
#
# all_region_dict = {}
# for litera in all_region_href:
#     href = litera.find('a').get('href')
#     text = litera.text
#     all_region_dict[text] = 'https://www.gismeteo.ru' + href
#

# # Создаём json файл для записи нашего словаря со ссылками
# with open('all_region_href.json', 'w', encoding='utf-8') as file:
#     json.dump(all_region_dict, file, indent=4, ensure_ascii=False)
'''РОССИЯ И ЕЁ РЕГИОНЫ'''


'''В С Е ОБЛАСТИ И ИХ ДЕРЕВНИ'''
# Читаем наш json файл со ссылками
# with open('all_region_href.json', encoding='utf-8') as file:
#     all_region_href = json.load(file)
#
# count = 0
# # Проходимся по каждому региону и берём оттуда ссылки на каждый город
# for region_name, region_href in all_region_href.items():
#     r = requests.get(region_href, headers=headers)
#     src = r.text
#
#     soup = BeautifulSoup(src, 'lxml')
#
#     try:
#         all_city_href = soup.find(class_='two-columns').find(class_='catalog-list').find_all(class_='catalog-item-link')
#
#         # Находим все ссылки на все пункты России
#         all_city_dict = {}
#         for litera in all_city_href:
#             href = litera.find('a').get('href')
#             text = litera.text
#             all_city_dict[text] = 'https://www.gismeteo.ru' + href
#     except:
#         all_city_href = soup.find(class_='groups').find(class_='catalog-list').find_all(class_='catalog-item-link')
#         # Находим все ссылки на все пункты России
#         all_city_dict = {}
#         for litera in all_city_href:
#             href = litera.find('a').get('href')
#             text = litera.text
#             all_city_dict[text] = 'https://www.gismeteo.ru' + href
#
#     with open(f'City_link/{region_name}.json', 'w', encoding='utf-8') as file:
#         json.dump(all_city_dict, file, indent=4, ensure_ascii=False)
'''В С Е ОБЛАСТИ И ИХ ДЕРЕВНИ'''

'''ВСЕ ДЕРЕВНИ И ИХ ССЫЛКИ'''
# p = Path('C:\П\Yandexparser\City_link')
# for x in p.rglob('*'):
#
#     city_name = str(x)[28:-5]
#     print(f'Приступаю к {city_name}...')
#     try:
#         os.mkdir(f'C:\П\Yandexparser\Village_link/{city_name}')
#
#         with open(x, encoding='utf-8') as file:
#             all_village_href = json.load(file)
#
#         for village_name, village_href in all_village_href.items():
#             r = requests.get(village_href, headers=headers)
#             src = r.text
#
#             soup = BeautifulSoup(src, 'lxml')
#
#             try:
#                 all_village_href = soup.find(class_='two-columns').find(class_='catalog-list').find_all(class_='catalog-item-link')
#
#                 # Находим все ссылки на все пункты России
#                 all_village_dict = {}
#                 for litera in all_village_href:
#                     href = litera.find('a').get('href')
#                     text = litera.text
#                     all_village_dict[text] = 'https://www.gismeteo.ru' + href
#
#             except:
#                 all_village_href = soup.find(class_='groups').find(class_='catalog-list').find_all(class_='catalog-item-link')
#                 # Находим все ссылки на все пункты России
#                 all_village_dict = {}
#                 for litera in all_village_href:
#                     href = litera.find('a').get('href')
#                     text = litera.text
#                     all_village_dict[text] = 'https://www.gismeteo.ru' + href
#
#             with open(f'Village_link/{city_name}/{village_name}.json', 'w', encoding='utf-8') as file:
#                 json.dump(all_village_dict, file, indent=4, ensure_ascii=False)
#
#             if random.randint(1, 6) > 4:
#                 print(f'{village_name} добавлен в {city_name}...')
#
#         print(f'{city_name} обработан...')
#     except:
#         continue
# print('Все village упешно записаны!')

'''ВСЕ ДЕРЕВНИ И ИХ ССЫЛКИ В ОДНОМ ФАЙЛЕ'''
# p = Path('C:\П\Yandexparser\Village_link')
#
# with open('all_village_href.json', 'a', encoding='utf-8') as file:
#     dict_with_name = {}
#     for village_href in p.rglob('*.json'):
#         with open(village_href, encoding='utf-8') as village_dict:
#             href = json.load(village_dict)
#             for village_name, village_asdf in href.items():
#                 dict_with_name[village_name] = village_asdf
#     json.dump(dict_with_name, file, indent=4, ensure_ascii=False)
'''ВСЕ ДЕРЕВНИ И ИХ ССЫЛКИ В ОДНОМ ФАЙЛЕ'''

# with open('all_village_href.json', encoding='utf-8') as file:
#     all_village_href = json.load(file)
#
# village = input('Введите название города: ')
#
# if village in all_village_href:
#     href = all_village_href[village]
#     r = requests.get(href, headers=headers)
#     soup = BeautifulSoup(r.text, 'lxml')
#
#     weather_today = soup.find(class_='widget-items')
#
#     time_data = weather_today.find(class_='widget-row-time').find_all(class_='row-item')
#     time_list = []
#     for item in time_data:
#         time = (item.text[:-2] + ':' + item.text[-2:])
#         time_list.append(time)
#
#     temperature_data = weather_today.find(class_='widget-row-chart-temperature').find_all(class_='unit_temperature_c')
#     temperature_list = []
#     for item in temperature_data[1:]:
#         temperature = item.text
#         temperature_list.append(temperature)
#
#     weather_at_whis_day = {}
#     for i in range(0, len(time_list)-1):
#         weather_at_whis_day[time_list[i]] = temperature_list[i]
#
#     print(weather_at_whis_day)
# else:
#     print('Проверьте правильность написания пункта')