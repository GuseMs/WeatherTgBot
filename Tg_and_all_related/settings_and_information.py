from aiogram import F, Router
from aiogram.filters import Command
from Function.minor_features import *
from localisation import *
from state_class import Help
from aiogram.fsm.context import FSMContext
from config import ADMINS
from loader import bot

settings_and_info = Router()


@settings_and_info.message(Command('settings'))
async def settings(message: Message) -> None:
    await message.answer('Настройки:',
                         reply_markup=create_double_level_inline([support, author], 'settings').as_markup())


@settings_and_info.callback_query(F.data.startswith('settings_'))
async def help_users(call: CallbackQuery) -> None:
    text = call.data.split('_')[1]
    if text == support:
        await update_text(call.message, 'Вы обратились в поддержку.\nВы точно уверены?',
                          create_inline(help, cancel).as_markup())
    elif text == author:
        await call.message.answer(f'Над проектом работали:\n@Gu7e\n@Veiperyt')
    else:
        await call.answer()
    await call.answer()


@settings_and_info.callback_query(F.data == cancel)
async def call_cancel(call: CallbackQuery) -> None:
    await call.answer()
    await update_text(call.message, 'Настройки: ',
                      create_double_level_inline([support, author], 'settings').as_markup())


@settings_and_info.callback_query(F.data == help)
async def call_help(call: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(Help.wait_for_message.state)
    await call.answer()
    await call.message.answer('Хорошо.\nОпишите вашу проблему')


@settings_and_info.message(Help.wait_for_message)
async def send_msg(message: Message, state: FSMContext) -> None:
    text = message.text
    user = message.from_user.username
    await state.clear()
    await bot.send_message(ADMINS[0], f'Вам сообщение от {user}:\n'
                                      f'\'{text}\'')
    await message.answer('Сообщение отправлено администратору на проверку.\nВскоре он с вами свяжется!')
    await message.answer('Настройки', reply_markup=create_double_level_inline([support, author], 'settings').as_markup())


@settings_and_info.message(Command('information'))
async def information_func(message: Message):
    await message.answer(information_about_project, reply_markup=create_double_level_inline(['Линейная',
                                                                                             'Метод опорных векторов',
                                                                                             'Random Forest',
                                                                                             'XGBoost',
                                                                                             'K-ближайших соседей',
                                                                                             'С использованием дерева',
                                                                                             'Результаты оценки точности'
                                                                                             ], 'method').adjust(1).as_markup())


@settings_and_info.callback_query(F.data.startswith('method_'))
async def method(call: CallbackQuery):
    text = call.data.split('_')[1]

    inlinemarkup = create_double_level_inline(['Линейная',
                                               'Метод опорных векторов',
                                               'Random Forest',
                                               'XGBoost',
                                               'K-ближайших соседей',
                                               'С использованием дерева',
                                               'Результаты оценки точности'
                                               ], 'method').adjust(1).as_markup()

    if text == 'Линейная':

        await update_text(call.message, information_about_linear, inlinemarkup)

    elif text == 'Метод опорных векторов':

        await update_text(call.message, information_about_svr, inlinemarkup)

    elif text == 'Random Forest':
        await update_text(call.message, information_about_randomforest, inlinemarkup)

    elif text == 'XGBoost':
        await update_text(call.message, information_about_xgboost, inlinemarkup)

    elif text == 'K-ближайших соседей':
        await update_text(call.message, information_about_knear, inlinemarkup)

    elif text == 'С использованием дерева':
        await update_text(call.message, information_about_tree, inlinemarkup)

    elif text == 'Результаты оценки точности':
        await update_text(call.message, information_about_result, inlinemarkup)
