BOT_TOKEN = '6819328909:AAGEYX-CbC7kKuGCzKjDjRa8UkfWB8LMgus'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/119.0.0.0 Safari/537.36'
}

columns = ['Год', 'День', 'Скорость_ветра(м/с)', 'Давление', 'Влажность', 'Осадки_(м/м)', 'Населённый_пункт_aleksandrovskaya-2', 'Населённый_пункт_beloostrov', 'Населённый_пункт_kolpino-2', 'Населённый_пункт_komarovo-3', 'Населённый_пункт_krasnoye-selo', 'Населённый_пункт_kronshtadt', 'Населённый_пункт_levashovo', 'Населённый_пункт_lisy-nos', 'Населённый_пункт_lomonosov', 'Населённый_пункт_metallostroy', 'Населённый_пункт_molodezhnoye', 'Населённый_пункт_pargolovo', 'Населённый_пункт_pavlovsk-4', 'Населённый_пункт_pesochny', 'Населённый_пункт_petergof', 'Населённый_пункт_petro-slavyanka', 'Населённый_пункт_pontonny', 'Населённый_пункт_pushkin', 'Населённый_пункт_repino', 'Населённый_пункт_sankt-peterburg', 'Населённый_пункт_sankt-peterburg-pulkovo-airport', 'Населённый_пункт_saperny', 'Населённый_пункт_serovo', 'Населённый_пункт_sestroretsk', 'Населённый_пункт_shushary', 'Населённый_пункт_smolyachkovo', 'Населённый_пункт_solnechnoye', 'Населённый_пункт_strelna', 'Населённый_пункт_tyarlevo', 'Населённый_пункт_ushkovo', 'Населённый_пункт_ust-izhora', 'Населённый_пункт_zelenogorsk-3', 'Месяц_april', 'Месяц_august', 'Месяц_december', 'Месяц_february', 'Месяц_january', 'Месяц_july', 'Месяц_june', 'Месяц_march', 'Месяц_may', 'Месяц_november', 'Месяц_october', 'Месяц_september', 'Время_суток_вечер', 'Время_суток_день', 'Время_суток_ночь', 'Время_суток_сейчас', 'Время_суток_утро', 'Направление_ветра_Восточный ветер', 'Направление_ветра_Западный ветер', 'Направление_ветра_Северный ветер', 'Направление_ветра_Северо-восточный ветер', 'Направление_ветра_Северо-западный ветер', 'Направление_ветра_Юго-восточный ветер', 'Направление_ветра_Юго-западный ветер', 'Направление_ветра_Южный ветер', 'Направление_ветра_нет']

city_dict = {
    'александровская-2': 'aleksandrovskaya-2',
    'белоостров': 'beloostrov',
    'колпино-2': 'kolpino-2',
    'комарово-3': 'komarovo-3',
    'красное село': 'krasnoye-selo',
    'кронштадт': 'kronshtadt',
    'левашово': 'levashovo',
    'лисы-нос': 'lisy-nos',
    'ломоносов': 'lomonosov',
    'металлострой': 'metallostroy',
    'молодежное': 'molodezhnoye',
    'парголово': 'pargolovo',
    'павловск-4': 'pavlovsk-4',
    'песочный': 'pesochny',
    'петергоф': 'petergof',
    'петро-славянка': 'petro-slavyanka',
    'понтонный': 'pontonny',
    'пушкин': 'pushkin',
    'репино': 'repino',
    'санкт-петербург': 'sankt-peterburg',
    'санкт-петербург-пулково-аэропорт': 'sankt-peterburg-pulkovo-airport',
    'саперный': 'saperny',
    'серово': 'serovo',
    'сестрорецк': 'sestroretsk',
    'шушары': 'shushary',
    'смолячково': 'smolyachkovo',
    'солнечное': 'solnechnoye',
    'стрельна': 'strelna',
    'тярлево': 'tyarlevo',
    'ушково': 'ushkovo',
    'уст-изхода': 'ust-izhora',
    'зеленогорск-3': 'zelenogorsk-3'
}


ADMINS = [5355657752, ]

a = {'a': 1, 'b': 4}
print(a['a'])