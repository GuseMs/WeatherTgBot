import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import re

#
title = pd.read_csv('City/Sarov.csv')

title1 = title


title1['Месяц'] = title1['Месяц'].astype('category')

title1['Время_суток'] = title1['Время_суток'].astype('category')

title1['Температура'] = title1['Температура'].apply(lambda x: None if not re.search(r'-?\d+',
                                                                                    str(x)) else re.search(r'-?\d+',
                                                                                                           str(x)).group())

title1['Направление_ветра'] = title1['Направление_ветра'].astype('category')

title1['Осадки_(м/м)'] = title1['Осадки_(м/м)'].apply(
    lambda x: re.search(r'\d+\.\d+', str(x)).group() if re.search(r'\d+\.\d+', str(x)) else 0)

features = ['Месяц', 'День', 'Время_суток', 'Скорость_ветра(м/с)', 'Направление_ветра', 'Давление', 'Влажность',
            'Осадки_(м/м)']
target = 'Температура'

X_train, X_test, y_train, y_test = train_test_split(title1[features], title1[target], test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

plt.scatter(X_test['Год'], y_test, label='Actual data')
plt.scatter(X_test['Год'], y_pred, color='red', label='Predicted data')
plt.xlabel('Год')
plt.ylabel('Температура')
plt.legend()
plt.show()

# title = pd.read_csv('City/Sarov.csv')
#
# '''ПЕРВЫЕ N СТРОК'''
# print(title.head(19))
#
# '''ПОСЛЕДНИЕ N СТРОК'''
# print(title.tail(10))

# '''ТИП СТОЛБЦА'''
# print(title.dtypes)

# '''ИНФОРМАЦИЯ О SERIES/DATAFRAME'''
# title.info()

# '''СЧИТАТЬ ИНФОРМАЦИЮ ИЗ ФАЙЛА'''
# title.to_excel('title.xlsx', index=False)

# '''СРЕДНИЙ ПОКАЗАТЕЛЬ'''
# print(title.describe())
'''count — это количество заполненных строк в каждом столбце. В столбце с данными есть пропуски.
mean — среднее значение.
std — стандартное отклонение. Важный статистический показатель, показывающий разброс значений.
min и max — минимальное и максимальное значение.
25%, 50% и 75% — значения по процентилям. Процентиль — это число, которое показывает распределение значений в выборке. Например, в выборке с мобильным интернетом процентиль 25% показывает, что 25% от всех значений скорости интернета меньше, чем 24,4.
'''

# print(title.sort_values('Год', ascending=True)) #ascending - фильтрация по убыванию или возрастанию

# print(title.dropna()) # dropna() - удаление СТРОЧКИ, содержащей NaN{None}

# print(title[['Год', 'Месяц']]) # - Определённые столбцы

# print(title.count()) # - Кол-во значений в столбцах

# print(title.sum()) # - Подсчитать значения в столбцах

# print(title['Скорость_ветра(м/с)'].mean()) - Среднее столбца

# print(title['Скорость_ветра(м/с)'].median()) - Медиана (делит поровну)

# print(*title.groupby('Месяц')).mean()

# pd.set_option('display.max_columns', None) - При выводе в консоль удаляет ограничения. В копаемся в настройках вывода

# pd.reset_option('display.max_columns') - Ресет настроек (выбранных параметров)
