from telebot import TeleBot, types
import requests
import os
from dotenv import load_dotenv


load_dotenv()


bot = TeleBot(token=os.getenv('TOKEN'))
URL = 'https://api.thecatapi.com/v1/images/search'


def get_new_image():
    response = requests.get(URL).json()
    image_url = response[0].get('url')
    return image_url


@bot.message_handler(commands=['newcat'])
def new_cat(message):
    chat = message.chat
    bot.send_photo(chat.id, get_new_image())


@bot.message_handler(commands=['start'])
def wake_up(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_new_cat = types.KeyboardButton('/newcat')
    keyboard.add(button_new_cat)

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Спасибо, что включили меня, {message.chat.first_name}',
        reply_markup=keyboard,
    )

    bot.send_photo(message.chat.id, get_new_image())


@bot.message_handler(content_types=['text'])
def say_hi(message):
    bot.send_message(chat_id=message.chat.id, text='Привет, я KittyBot!')


bot.polling()
