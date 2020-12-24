from glob import glob
from random import choice
from utils import get_smile, get_keyboard


def greet_user(update, context):
    get_name = update.effective_chat.first_name
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f'Здравствуй {get_name} {context.user_data["emoji"]}', 
                                reply_markup=get_keyboard())

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    user_text = update.message.text
    update.message.reply_text(f'{user_text} {context.user_data["emoji"]}', reply_markup=get_keyboard())

def send_cat_picture(update, context):
    cat_photos_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'))    