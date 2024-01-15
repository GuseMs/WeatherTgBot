from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from Function.extract_temperature import extract_temperature
from Function.extract_precipitation import extract_precipitation
import pandas as pd
import numpy as np


title = pd.read_csv('C:\П\Tg_weather_bot/All_city_dataset.csv')

title[['Температура']] = title[['Температура']].apply(lambda x: x.apply(extract_temperature))
title[['Осадки_(м/м)']] = title[['Осадки_(м/м)']].apply(lambda x: x.apply(extract_precipitation))

features = title[
    ['Населённый_пункт', 'Год', 'Месяц', 'День', 'Время_суток', 'Скорость_ветра(м/с)', 'Давление', 'Влажность', 'Погода']
    ]

target = title[['Температура']]

features = pd.get_dummies(features, columns=['Населённый_пункт', 'Время_суток', 'Месяц', 'Погода'])

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

y_train, y_test = np.ravel(y_train), np.ravel(y_test)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

svm_regressor = SVR(kernel='linear', C=1.0)
svm_regressor.fit(x_train_scaled, y_train)

y_pred = svm_regressor.predict(x_test_scaled)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'mse: {mse}\nmae: {mae}\nr2: {r2}')

# '''БОЛЬШЕ 2 ЧАСОВ!!!!!!'''
# mse: 20.619380029622246
# mae: 3.5527939773734887
# r2: 0.7780848007213678