from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import re
import pandas as pd

title = pd.read_csv('C:\П\Yandexparser\City/asdf.csv')


def extract_temperature(temperaturestr):
    match = re.search(r'(-?\d+)', temperaturestr)
    return int(match.group(1)) if match else None


title[['Температура']] = title[['Температура']].apply(lambda x: x.apply(extract_temperature))

features = title[['Населённый_пункт', 'Год', 'Месяц', 'День', 'Время_суток', 'Скорость_ветра(м/с)', 'Давление', 'Влажность']]
target = title[['Температура']]

features = pd.get_dummies(features, columns=['Населённый_пункт','Время_суток', 'Месяц'])

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

'''Объект Регрессии'''
random_forest_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

random_forest_regressor.fit(X_train, y_train)

y_pred = random_forest_regressor.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f'mse: {mse}\nr2: {r2}\nmae: {mae}')