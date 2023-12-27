from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
from Function.extract_precipitation import extract_precipitation
from Function.extract_temperature import extract_temperature
import re
import pandas as pd

title = pd.read_csv('C:\П\Yandexparser\City/asdf.csv')

title[['Температура']] = title[['Температура']].apply(lambda x: x.apply(extract_temperature))
title[['Осадки_(м/м)']] = title[['Осадки_(м/м)']].apply(lambda x: x.apply(extract_precipitation))


features = title[['Населённый_пункт', 'Год', 'Месяц', 'День', 'Время_суток', 'Скорость_ветра(м/с)', 'Направление_ветра', 'Давление', 'Влажность', 'Осадки_(м/м)']]
target = title['Температура']

features = pd.get_dummies(features, columns=['Населённый_пункт', 'Месяц', 'Время_суток', 'Направление_ветра'])

columns = features.columns.tolist()

print(columns)
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)


'''Объект Регрессии'''
random_forest_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

random_forest_regressor.fit(X_train, y_train)

y_pred = random_forest_regressor.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

joblib.dump(random_forest_regressor, 'trained_random_forest_regressor.joblib')

print(f'mse: {mse}\nr2: {r2}\nmae: {mae}')


# Без осадков
# ~2-3 минуты
# mse: 0.6080145655702531
# r2: 0.9934562691366572
# mae: 0.3745508311722234

# С осадками
# mse: 0.6103999552230452
# r2: 0.9934305964821256
# mae: 0.3748954271534916


# Все параметры
# mse: 0.6029107371406183
# r2: 0.9935111988727316
# mae: 0.3734998787290808


# mse: 0.6013868747551261
# r2: 0.9935275993767461
# mae: 0.3733093901005615