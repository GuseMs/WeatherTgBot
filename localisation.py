cancel = 'Отмена'
help = 'Обратиться'
support = 'Поддержка'
author = 'Авторы'


information_about_project = '''Информация о проекте

    Данный Telegram-бот по предсказанию погоды использует классические модели машинного обучения для предсказания.

    Обучение алгоритмов происходило на исторических данных полученных с сайта: Pogoda1 за период с 1 января 2018 года по 21 января 2024 года в 20 городах России.

    В качестве алгоритмов тестировались следующие:
    1. Линейная регрессия
    2. Метод опорных векторов
    3. Случайный лес
    4. XGBoost
    5. Метод k ближайших соседей
    6. Дерево решений
        
    По итогам обучения были получены оценки для каждой модели и выбрана наилучшая, которая сейчас используется в Telegram-боте: Метод случайного леса (random forest).

Подробнее о моделях и процессе их обучения:'''


information_about_linear = '''Описание:
        Линейная регрессия - это метод, предполагающий линейную зависимость между входными признаками и целевой переменной. Модель стремится подобрать линию (в случае одного признака) или гиперплоскость (в случае нескольких признаков), которая наилучшим образом соответствует данным.

        Пример:
        
        
        from sklearn.linear_model import LinearRegression
        import numpy as np
        
        # Генерация данных
        X = np.array([[1], [2], [3]])
        y = np.array([2, 3, 4])
        
        # Создание и обучение модели
        model = LinearRegression()
        model.fit(X, y)
        
        # Предсказание для новых данных
        new_data = np.array([[4]])
        prediction = model.predict(new_data)
        print(prediction)
        
        
        Основные шаги приведенного примера:
        Создаются массивы X и y, где X содержит векторы признаков (в данном случае, одномерные), а y содержит соответствующие целевые значения.
        Создается объект модели LinearRegression, и модель обучается на предоставленных данных.
        Создается новый массив new_data с данными, для которых мы хотим сделать предсказание. 
        Затем вызывается метод predict модели, чтобы получить предсказание для новых данных, и результат выводится на экран.'''


information_about_svr = '''Описание:
        Метод опорных векторов для регрессии (SVR) использует метод опорных векторов для построения модели. Он стремится создать "трубу" вокруг точек данных, в пределах которой должно находиться как можно больше наблюдений.

        Пример:


        from sklearn.svm import SVR
        import numpy as np

        # Генерация данных
        X = np.array([[1], [2], [3]])
        y = np.array([2, 3, 4])

        # Создание и обучение модели
        model = SVR(kernel='linear')
        model.fit(X, y)

        # Предсказание для новых данных
        new_data = np.array([[4]])
        prediction = model.predict(new_data)
        print(prediction)
        
        
        Основные шаги приведенного примера:
        Создаются массивы X и y, где X содержит векторы признаков (в данном случае, одномерные), а y содержит соответствующие целевые значения.
        Создается объект модели SVR с использованием линейного ядра (linear kernel), и модель обучается на предоставленных данных.
        Создается новый массив new_data с данными, для которых мы хотим сделать предсказание. 
        Затем вызывается метод predict модели, чтобы получить предсказание для новых данных, и результат выводится на экран.'''


information_about_randomforest = '''Описание:
        Случайный лес - это ансамбльный метод, который строит несколько деревьев решений и усредняет их предсказания для улучшения качества модели.

        Пример:


        from sklearn.ensemble import RandomForestRegressor
        import numpy as np

        # Генерация данных
        X = np.array([[1], [2], [3]])
        y = np.array([2, 3, 4])

        # Создание и обучение модели
        model = RandomForestRegressor(n_estimators=100)
        model.fit(X, y)

        # Предсказание для новых данных
        new_data = np.array([[4]])
        prediction = model.predict(new_data)
        print(prediction)
        
        Основные шаги приведенного примера:
        Создаются массивы X и y, где X содержит векторы признаков (в данном случае, одномерные), а y содержит соответствующие целевые значения.
        Создается объект модели RandomForestRegressor с указанием параметра n_estimators=100 (количество деревьев в лесу), и модель обучается на предоставленных данных.
        Создается новый массив new_data с данными, для которых мы хотим сделать предсказание. 
        Затем вызывается метод predict модели, чтобы получить предсказание для новых данных, и результат выводится на экран.'''


information_about_xgboost = '''Описание:
        XGBoost - это эффективная реализация градиентного бустинга, комбинирующая несколько слабых моделей для создания более сильной.

        Пример:


        from xgboost import XGBRegressor
        import numpy as np

        # Генерация данных
        X = np.array([[1], [2], [3]])
        y = np.array([2, 3, 4])

        # Создание и обучение модели
        model = XGBRegressor()
        model.fit(X, y)

        # Предсказание для новых данных
        new_data = np.array([[4]])
        prediction = model.predict(new_data)
        print(prediction)
        
        
        Основные шаги приведенного примера:
        Создаются массивы X и y, где X содержит векторы признаков (в данном случае, одномерные), а y содержит соответствующие целевые значения.
        Создается объект модели XGBRegressor, и модель обучается на предоставленных данных.
        Создается новый массив new_data с данными, для которых мы хотим сделать предсказание. Затем вызывается метод 
        predict модели, чтобы получить предсказание для новых данных, и результат выводится на экран.'''


information_about_knear = '''Описание:
        Метод K-ближайших соседей использует близость объектов в пространстве признаков для предсказания значений целевой переменной.

        Пример:


        from sklearn.neighbors import KNeighborsRegressor
        import numpy as np

        # Генерация данных
        X = np.array([[1], [2], [3]])
        y = np.array([2, 3, 4])

        # Создание и обучение модели
        model = KNeighborsRegressor(n_neighbors=2)
        model.fit(X, y)

        # Предсказание для новых данных
        new_data = np.array([[4]])
        prediction = model.predict(new_data)
        print(prediction)
        
        
        Основные шаги приведенного примера:
        Создаются массивы X и y, где X содержит векторы признаков (в данном случае, одномерные), а y содержит соответствующие целевые значения.
        Создается объект модели KNeighborsRegressor с указанием параметра n_neighbors=2 (количество ближайших соседей для учета при предсказании), и затем модель обучается на предоставленных данных.
        Создается новый массив new_data с данными, для которых мы хотим сделать предсказание. 
        Затем вызывается метод predict модели, чтобы получить предсказание для новых данных, и результат выводится на экран.'''


information_about_tree = '''
        Описание:
        
        Метод K-ближайших соседей (K-Nearest Neighbors, KNN) использует близость объектов в пространстве признаков для предсказания значений целевой переменной. 
        Он основывается на принципе, что объекты с похожими признаками имеют похожие значения целевой переменной.
        
        Пример кода на Python:
        
        
        from sklearn.neighbors import KNeighborsRegressor
        import numpy as np
        
        # Генерация данных
        X = np.array([[1], [2], [3]])
        y = np.array([2, 3, 4])
        
        # Создание и обучение модели
        model = KNeighborsRegressor(n_neighbors=2)
        model.fit(X, y)
        
        # Предсказание для новых данных
        new_data = np.array([[4]])
        prediction = model.predict(new_data)
        print(prediction)
        
        
        В данном примере используется библиотека scikit-learn для создания модели K-ближайших соседей для регрессии (KNeighborsRegressor). 
        Обучающие данные представлены признаками X и соответствующими значениями целевой переменной y. 
        Модель обучается на этих данных, и затем можно делать предсказания для новых данных, таких как new_data. 
        В данном случае, для нового значения 4, модель предсказывает соответствующее значение.'''


information_about_result = '''Линейная регрессия:                mse: 21.089428036856084
                                                            mae: 3.670171117685546
                                                            r2:     0.7856412833501571
    
Метод опорных векторов:     mse: 20.619380029622246
                                                            mae: 3.5527939773734887
                                                            r2:     0.7780848007213678
                                    
Random Forest:                            mse: 0.647060368109017
                                                            mae: 0.37735156180868945
                                                            r2:     0.9934231013823407
                                                            
XGBoost:                                          mse: 56.34247505974757
                                                            mae: 6.048585251484516
                                                            r2:     0.42731966814953404
                        
K-ближайших соседей:             mse: 5.387472966994072
                                                            mae:0.8922997964781878
                                                            r2:     0.9452402507468509
        
С использованием дерева:     mse: 1.1662684718166534
                                                            mae: 0.3835412795327847
                                                            r2:     0.9881457281605319'''