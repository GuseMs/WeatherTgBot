import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from Function.extract_temperature import extract_temperature

title = pd.read_csv('C:\П\Yandexparser\City/asdf.csv')

title[['Температура']] = title[['Температура']].apply(lambda x: x.apply(extract_temperature))

features = title[
    ['Населённый_пункт', 'Год', 'Месяц', 'День', 'Время_суток', 'Скорость_ветра(м/с)', 'Давление', 'Влажность']]

target = title[['Температура']]

features = pd.get_dummies(features, columns=['Населённый_пункт', 'Время_суток', 'Месяц'])

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

regression = LinearRegression()

regression.fit(X_train, y_train)
y_pred = regression.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f'Среднеквадратичное отклонение: {mse}')
print(f'Абсолютное отклонение: {mae}')
print(f'Рассеивание: {r2}')


plt.scatter(y_pred, y_test, color='black')
plt.xlabel('Фактическое значение')
plt.ylabel('Предсказанное значение')
plt.title('Сложно это всё...')
plt.show()