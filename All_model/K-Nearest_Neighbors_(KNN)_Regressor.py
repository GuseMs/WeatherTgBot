from sklearn.neighbors import KNeighborsRegressor
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

features = pd.get_dummies(features, columns=['Населённый_пункт', 'Месяц', 'Время_суток'])

target = title[['Температура']]

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

kn_regressor = KNeighborsRegressor(n_neighbors=5)
kn_regressor.fit(x_train, y_train)

y_pred = kn_regressor.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'mse: {mse}\nmae: {mae}\n r2: {r2}')


# выполняется > 3 минут!!!!!
# mse: 5.981507863952686
# mae: 0.9632530457657791
#  r2: 0.935624276398766