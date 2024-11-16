from telebot import TeleBot, types
import logging
import requests
import os
from dotenv import load_dotenv
from random import randint


load_dotenv()


bot = TeleBot(token=os.getenv('TOKEN'))
URLs = ['https://api.thecatapi.com/v1/images/search', 'https://api.thedogapi.com/v1/images/search']


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)


def get_new_image():
    num = randint(0, 1)
    try:
        response = requests.get(URLs[num])
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        response = requests.get(URLs[1-num])

    response = response.json()
    image_url = response[0].get('url')
    return image_url


@bot.message_handler(commands=['newpet'])
def new_cat(message):
    chat = message.chat
    bot.send_photo(chat.id, get_new_image())


@bot.message_handler(commands=['start'])
def wake_up(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_new_cat = types.KeyboardButton('/newpet')
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


def main():
    bot.polling()


if __name__ == '__main__':
    main()
