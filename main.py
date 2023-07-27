import telebot
from time_weather import time_weather_message
from crypto import crypto_message

bot = telebot.TeleBot("6553910401:AAHeGBhw7j0MbEUSuL7yt8LU2TpzCeSvRCg")


@bot.message_handler(commands=['time_weather'])
def send_message(message):
    bot.reply_to(message, time_weather_message())


@bot.message_handler(commands=['crypto'])
def send_message(message):
    bot.reply_to(message, crypto_message())


time_weather_message()
crypto_message()

bot.infinity_polling()
