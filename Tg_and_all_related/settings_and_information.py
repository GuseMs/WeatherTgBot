from loder import dp, bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext, filters
from Tg_and_all_related.tg_bot import Help
from config import ADMINS
from Function.Tg_Keyboard import create_inline, create_inline_settings, update_text


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
    await message.answer('Информация о всех функциях')
    # Можновывести инлайн кнопочки с названиями моделей/алгоритмов