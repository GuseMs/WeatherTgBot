from loder import dp, bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext, filters
from Tg_and_all_related.tg_bot import Help
from config import ADMINS
from Function.Tg_Keyboard import create_inline, create_inline_settings, update_text, create_double_level_inline


cancel = 'Отмена'
help = 'Обратиться'
support = 'Поддержка'
tools = 'Инструменты'
author = 'Авторы'


@dp.message_handler(commands='settings')
async def settings(message: Message):
    await message.answer('Настройки:', reply_markup=create_inline_settings(support, tools, author))


@dp.callback_query_handler(filters.Text(startswith='settings_'))
async def help_users(call: CallbackQuery):
    text = call.data.split('_')[1]
    if text == support:
        await update_text(call.message, 'Вы обратились в поддержку.\nВы точно уверены?', create_inline(help, cancel))
    elif text == tools:
        id = call.message.from_user.id

#       Большой запрос к DB
        await update_text(call.message, 'Инструменты:', create_inline(cancel))
    elif text == author:
        await call.answer(f'Над проектом работали:\n@Gu7e\n@Veiperyt')
    else:
        await call.answer()
    await call.answer()


@dp.callback_query_handler(text=cancel)
async def call_cancel(call: CallbackQuery):
    await call.answer()
    await update_text(call.message, 'Настройки: ', create_inline_settings(support, tools, author))


@dp.callback_query_handler(text=help)
async def call_help(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer('Хорошо.\nОпишите вашу проблему')
    await state.set_state(Help.wait_for_message.state)


@dp.message_handler(state=Help.wait_for_message)
async def send_msg(message: Message, state: FSMContext):
    text = message.text
    user = message.from_user.username
    await bot.send_message(ADMINS[0], f'Вам сообщение от {user}:\n'
                                      f'\'{text}\'')
    await message.answer('Сообщение отправлено администратору на проверку.\nВскоре он с вами свяжется!')
    await message.answer('Настройки', reply_markup=create_inline_settings(support, tools))
    await state.finish()


@dp.message_handler(commands='information')
async def information_func(message: Message):
    await message.answer('Использованные методы обучения в проекте:', reply_markup=create_double_level_inline(['Линейная',
                           'Метод опорных векторов',
                           'Random Forest',
                           'XGBoost',
                           'K-ближайших соседей',
                           'С использованием дерева'
                           ], 'method'))


@dp.callback_query_handler(filters.Text(startswith='method_'))
async def method(call: CallbackQuery):
    text = call.data.split('_')[1]

    inlinemarkup = create_double_level_inline(['Линейная',
                                               'Метод опорных векторов',
                                               'Random Forest',
                                               'XGBoost',
                                               'K-ближайших соседей',
                                               'С использованием дерева'
                                               ], 'method')

    if text == 'Линейная':

        await update_text(call.message, '''Описание:
        Линейная регрессия - это метод, предполагающий линейную зависимость между входными признаками и целевой переменной. Модель стремится подобрать линию (в случае одного признака) или гиперплоскость (в случае нескольких признаков), которая наилучшим образом соответствует данным.

        Пример:
        
        python
        Copy code
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
        Затем вызывается метод predict модели, чтобы получить предсказание для новых данных, и результат выводится на экран.''', inlinemarkup)

        await call.answer()

    elif text == 'Метод опорных векторов':

        await update_text(call.message, '''Описание:
        Метод опорных векторов для регрессии (SVR) использует метод опорных векторов для построения модели. Он стремится создать "трубу" вокруг точек данных, в пределах которой должно находиться как можно больше наблюдений.

        Пример:

        python
        Copy code
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
        Затем вызывается метод predict модели, чтобы получить предсказание для новых данных, и результат выводится на экран.''', inlinemarkup)

    elif text == 'Random Forest':
        await update_text(call.message, '''Описание:
        Случайный лес - это ансамбльный метод, который строит несколько деревьев решений и усредняет их предсказания для улучшения качества модели.

        Пример:

        python
        Copy code
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
        Затем вызывается метод predict модели, чтобы получить предсказание для новых данных, и результат выводится на экран.''', inlinemarkup)

    elif text == 'XGBoost':
        await update_text(call.message, '''Описание:
        XGBoost - это эффективная реализация градиентного бустинга, комбинирующая несколько слабых моделей для создания более сильной.

        Пример:

        python
        Copy code
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
        predict модели, чтобы получить предсказание для новых данных, и результат выводится на экран.''', inlinemarkup)

    elif text == 'K-ближайших соседей':
        await update_text(call.message, '''Описание:
        Метод K-ближайших соседей использует близость объектов в пространстве признаков для предсказания значений целевой переменной.

        Пример:

        python
        Copy code
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
        Затем вызывается метод predict модели, чтобы получить предсказание для новых данных, и результат выводится на экран.''', inlinemarkup)

    elif text == 'С использованием дерева':
        await update_text(call.message, '''
        Описание:
        
        Метод K-ближайших соседей (K-Nearest Neighbors, KNN) использует близость объектов в пространстве признаков для предсказания значений целевой переменной. 
        Он основывается на принципе, что объекты с похожими признаками имеют похожие значения целевой переменной.
        
        Пример кода на Python:
        
        python
        Copy code
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
        В данном случае, для нового значения 4, модель предсказывает соответствующее значение.''', inlinemarkup)