import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from Function.minor_features import extract_precipitation
from Function.minor_features import extract_temperature
import pandas as pd

title = pd.read_csv('C:\П\Tg_weather_bot/All_city_dataset.csv')

title[['Температура']] = title[['Температура']].apply(lambda x: x.apply(extract_temperature))
title[['Осадки_(м/м)']] = title[['Осадки_(м/м)']].apply(lambda x: x.apply(extract_precipitation))

features = title[
    ['Населённый_пункт', 'Год', 'Месяц', 'День', 'Время_суток', 'Скорость_ветра(м/с)', 'Направление_ветра', 'Давление',
     'Влажность', 'Осадки_(м/м)', 'Погода']
    ]

target = title[['Температура']]

features = pd.get_dummies(features, columns=['Населённый_пункт', 'Время_суток', 'Месяц', 'Направление_ветра', 'Погода'])

columns = features.columns.to_list

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

'''Объект Регрессии'''
random_forest_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

random_forest_regressor.fit(X_train, y_train)

y_pred = random_forest_regressor.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

joblib.dump(random_forest_regressor, 'trained_random_forest_regressor.joblib')

print(f'mse: {mse}\nr2: {r2}\nmae: {mae}')

# mse: 0.5879784935164662
# r2: 0.9940236655127066
# mae: 0.36625159252342976