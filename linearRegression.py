import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import re

title = pd.read_csv('City/Sarov.csv')


def extract_temperature(temperaturestr):
    match = re.search(r'(-?\d+)', temperaturestr)
    return int(match.group(1)) if match else None


title[['Температура']] = title[['Температура']].apply(lambda x: x.apply(extract_temperature))

features = title[['Год', 'Месяц', 'День', 'Время_суток', 'Скорость_ветра(м/с)', 'Давление', 'Влажность']]
target = title[['Температура']]

features = pd.get_dummies(features, columns=['Время_суток', 'Месяц'])

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

regression = LinearRegression()

regression.fit(X_train, y_train)
y_pred = regression.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Отклонение: {mse}')
print(f'Рассеивание: {r2}')


plt.scatter(y_pred, y_test, color='black')
plt.xlabel('Фактическое значение')
plt.ylabel('Предсказанное значение')
plt.title('Сложно это всё...')
plt.show()