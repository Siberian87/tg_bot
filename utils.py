import settings
from random import choice
from emoji import emojize
from telegram import ReplyKeyboardMarkup

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def get_keyboard():
    my_keyboard = ReplyKeyboardMarkup([['Прислать котика']], resize_keyboard=True)
    return my_keyboard

