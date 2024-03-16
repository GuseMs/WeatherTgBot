import pandas as pd
import joblib
from config import columns
from Function.minor_features import extract_precipitation

def prediction_temperature(punkt: str, spisok: list) -> dict:
    model = joblib.load('trained_random_forest_regressor.joblib')

    dict_day_and_month = {}

    for spis in spisok:

        year, month, day, day_time, wind_speed, wind_direction, permission, vlaznost, osadki, pogoda = spis

        osadki_numeric = extract_precipitation(osadki)
        day = int(day, 10)

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
            'Осадки_(м/м)': [osadki_numeric],
            'Погода': [pogoda],
        })

        new_data = new_data.fillna(0)

        new_data = pd.get_dummies(new_data, columns=['Населённый_пункт', 'Время_суток', 'Месяц', 'Направление_ветра', 'Погода'])

        new_data = new_data.reindex(columns=columns, fill_value=0)

        predicted_temperature = model.predict(new_data)
        date = f'{day}.{month}.{year}'
        day_time = day_time.lower()
        temperature = float(predicted_temperature[0])

        if date not in dict_day_and_month:
            dict_day_and_month[date] = []

        dict_day_and_month[date].append({day_time: temperature})

    return dict_day_and_month
