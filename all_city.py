from bs4 import BeautifulSoup
import requests
from config import headers

link = 'https://pogoda1.ru/katalog/'

r = requests.get(link, headers=headers).text
soup_catalog = BeautifulSoup(r, 'lxml')

all_region = soup_catalog.find_all(class_='city-item')


for region in all_region[58:59]:
    all_city_spis = []
    href = region.find('a').get('href')
    print(f'\n\nОбрабатывается {region.text.strip()} (регион)\n')

    r_c = requests.get(href, headers=headers).text
    soup_region = BeautifulSoup(r_c, 'lxml')

    if soup_region.find(class_='regions-list') is None:
        all_area = []
        all_area.append(region)

    else:
        all_area = soup_region.find(class_='regions-list').find_all(class_='city-item')
    for area in all_area:
        href = area.find('a').get('href')
        print(f'Обрабатывается {area.text.strip()} (район)\n')

        r_a = requests.get(href, headers=headers).text
        soup_area = BeautifulSoup(r_a, 'lxml')

        try:
            all_city = soup_area.find(class_='panel-cities').find_all(class_='city-item')

            for city in all_city:
                href = city.find('a').get('href')
                all_city_spis.append(href)

        except Exception:
            href = href[37:]
            all_city_spis.append(href)

    with open('Peterburg.txt', 'a') as file:
        for item in all_city_spis:
            file.write(str(item) + '\n')
        print('Записано!')