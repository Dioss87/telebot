import telebot # import library
import requests
import logging

bot = telebot.TeleBot("7679283944:AAH7kCXfNvemAvG0ugqzHzb04LF_TyBkTgg") # connect token (from @fatherbot)

@bot.message_handler(content_types=["text"])
def get_text_message(message):
    if message.text.lower() == "Привет" or "":
        bot.send_message(message.from_user.id, "Привет, какой курс тебя интересует?")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, выбери курс")


bot.polling(non_stop=True)

