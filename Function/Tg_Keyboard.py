from loder import dp
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

cancel = 'Отмена'


def create_reply_keyboard(*buttons):
    Replymarkup = ReplyKeyboardMarkup(row_width=20, resize_keyboard=True)
    for i in buttons:
        Replymarkup.add(KeyboardButton(i))
    return Replymarkup


def create_inline_settings(*buttons):
    Inlinemarkup = InlineKeyboardMarkup(row_width=2)
    for i in buttons:
        Inlinemarkup.add(InlineKeyboardButton(f'{i}', callback_data=f'settings_{i}'))
    return Inlinemarkup


def create_double_level_inline(buttons: list, startswith: str):
    Inlinemarkup = InlineKeyboardMarkup(row_width=2)
    for i in buttons:
        Inlinemarkup.add(InlineKeyboardButton(f'{i}', callback_data=f'{startswith}_{i}'))
    return Inlinemarkup

def create_inline(*buttons):
    Inlinemarkup = InlineKeyboardMarkup(row_width=2)
    for i in buttons:
        Inlinemarkup.add(InlineKeyboardButton(f'{i}', callback_data=f'{i}'))
    return Inlinemarkup


def create_inline_url(url: dict):
    Inlinemarkup = InlineKeyboardMarkup(row_width=2)
    for i in url:
        Inlinemarkup.add(InlineKeyboardButton(f'{i}', url=f'{url[i]}'))
    Inlinemarkup.add(InlineKeyboardButton(f'{cancel}', callback_data=f'{cancel}'))
    return Inlinemarkup


async def update_text(message: Message, text: str, inlinemarkup):
    await message.edit_text(f'{text}', reply_markup=inlinemarkup)