import pandas as pd
import joblib
from config import columns
import re

def extract_precipitation(s):
    match = re.search(r'(-?\d+(\.\d+)?)', s)
    return float(match.group(1)) if match else float(0)


def prediction_temperature(tuple):

    model = joblib.load('C:\П\Yandexparser/trained_random_forest_regressor.joblib')

    temperatures = []
    for spis in tuple:


        punkt, year, month, day, day_time, wind_speed, wind_direction, permission, vlaznost, osadki = spis[0], spis[1], \
            spis[2], spis[3], spis[4], spis[6], spis[7], spis[8], spis[9], spis[10]

        osadki_numeric = extract_precipitation(osadki)
        new_data = pd.DataFrame({
            'Населённый_пункт': [punkt],
            'Год': [year],
            'Месяц': [month],
            'День': [day],
            'Время_суток': [day_time],
            'Скорость_ветра(м/с)': [wind_speed],
            'Направление_ветра': [wind_direction],
            'Давление': [permission],
            'Влажность': [vlaznost],
            'Осадки_(м/м)': [osadki_numeric]
        })

        new_data = new_data.fillna(0)

        new_data = pd.get_dummies(new_data, columns=['Населённый_пункт', 'Время_суток', 'Направление_ветра'])

        new_data = new_data.reindex(columns=columns, fill_value=0)

        predicted_temperature = model.predict(new_data)
        temperatures.append(float(predicted_temperature))

    return temperatures