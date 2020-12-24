import logging
import settings
from emoji import emojize
from glob import glob
from random import choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    get_name = update.effective_chat.first_name
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f'Здравствуй {get_name} {context.user_data["emoji"]}')

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    user_text = update.message.text
    update.message.reply_text(f'{user_text} {context.user_data["emoji"]}')

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']    

def send_cat_picture(update, context):
    cat_photos_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'))


def main():
    my_bot = Updater(settings.API_KEY, use_context=True)

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()