import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.tree import DecisionTreeRegressor, export_text, export_graphviz
from Function.extract_temperature import extract_temperature
import graphviz

title = pd.read_csv('C:\П\Yandexparser\City/asdf.csv')


title[['Температура']] = title[['Температура']].apply(lambda x: x.apply(extract_temperature))

features = title[['Населённый_пункт', 'Год', 'Месяц', 'День', 'Время_суток', 'Скорость_ветра(м/с)', 'Давление', 'Влажность']]
target = title[['Температура']]

features = pd.get_dummies(features, columns=['Населённый_пункт', 'Время_суток', 'Месяц'])

# Кормим модель
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

tree_regressor = DecisionTreeRegressor(random_state=42)

tree_regressor.fit(X_train, y_train)

y_pred = tree_regressor.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f'mse: {mse}\nr2: {r2}\nmae: {mae}')

# tree_rules = export_text(tree_regressor, feature_names=list(features.columns)) '''Дерево в строках'''

dota_data = export_graphviz(tree_regressor, out_file=None, feature_names=features.columns, filled=True, rounded=True, special_characters=True)

graph = graphviz.Source(dota_data)

graph.render('Дерево_решений')

graph.view('Дерево_решений')

# mse: 1.0936957779063041
# r2: 0.9882291457766627
# mae: 0.3819660814567436