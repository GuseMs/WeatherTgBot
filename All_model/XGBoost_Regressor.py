import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from Function.extract_temperature import extract_temperature
import pandas as pd

title = pd.read_csv('C:\П\Yandexparser\City/asdf.csv')

title[['Температура']] = title[['Температура']].apply(lambda x: x.apply(extract_temperature))

features = title[
    [
    'Населённый_пункт', 'Год', 'Месяц', 'День', 'Время_суток', 'Скорость_ветра(м/с)', 'Давление', 'Влажность'
    ]
]

features = pd.get_dummies(features, columns=['Населённый_пункт', 'Время_суток', 'Месяц'])
target = title[['Температура']]

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)


xg_reg = xgb.XGBRegressor(objective='reg:squarederror', colsample_bytree=0.3, learning_rate=0.1,
                          max_depth=5, alpha=10, n_estimators=10)

xg_reg.fit(x_train, y_train)


y_pred = xg_reg.predict(x_test)

'''Точность модели'''
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'mse: {mse}\nmae: {mae}\n r2: {r2}')


# mse: 47.408276114840476
# mae: 5.57642389505456
 # r2: 0.48977044768721956