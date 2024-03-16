import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from Function.minor_features import extract_temperature
from Function.minor_features import extract_precipitation

title = pd.read_csv('C:\П\Tg_weather_bot/All_city_dataset.csv')

title[['Температура']] = title[['Температура']].apply(lambda x: x.apply(extract_temperature))
title[['Осадки_(м/м)']] = title[['Осадки_(м/м)']].apply(lambda x: x.apply(extract_precipitation))

features = title[
    ['Населённый_пункт', 'Год', 'Месяц', 'День', 'Время_суток', 'Скорость_ветра(м/с)', 'Давление', 'Влажность', 'Погода']
    ]

target = title[['Температура']]

features = pd.get_dummies(features, columns=['Населённый_пункт', 'Время_суток', 'Месяц', 'Погода'])

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

regression = LinearRegression()

regression.fit(X_train, y_train)
y_pred = regression.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f'mse: {mse}\nr2: {r2}\nmae: {mae}')

# mse: 21.207644825558603
# r2: 0.7879696806353289
# mae: 3.6748441078496956
