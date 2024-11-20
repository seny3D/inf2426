import telebot
from telebot.types import Message

# скопируйте файл public_config.py в config.py и вставьте там ваш токен
from config import TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message: Message):
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + " " + message.from_user.last_name)

@bot.message_handler(content_types="text")
def dialog(message: Message):
    if message.text.lower() == "hello":
        bot.send_message(message.chat.id, "hi")
    else:
        bot.send_message(message.chat.id, "как вас зовут?")

bot.polling(non_stop=True)
