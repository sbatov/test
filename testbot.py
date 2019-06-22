from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from urllib import request
from urllib.parse import quote
from pyparsing import *
import re
import random
import lxml
import tqdm


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def talk_to_me(bot, update):

    text = 'Привет!'
    temp_string = update.message.text

    update.message.reply_text('Ваше обращение будет обработано')

def greet_user(bot, update):

    text = 'Привет!'

    print(text)

    update.message.reply_text(text)

    print('Привет!')

def main():
#
    mybot = Updater("836959260:AAGoAyTCcDUTwEcJmUVjvrNRCihScXc85nA", request_kwargs=PROXY)

    dp = mybot.dispatcher

    dp.add_handler(CommandHandler("start", greet_user))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()

    mybot.idle()


main()
