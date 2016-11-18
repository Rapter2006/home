#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weather import Weather
from news import News
from habrahabr import Habrahabr
from var9 import Var9
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

class Telegram(object):
    def help(self, bot, update):
        info_str = 'List of commands: ' + ', '.join(self.list_commands)
        update.message.reply_text(info_str)

    def weather(self, bot, update):
        weather = Weather()
        update.message.reply_text(weather.get_weather())

    def news(self, bot, update):
        news = News()
        update.message.reply_text(news.get_news(10))

    def habrahabr(self, bot, update):
        habr = Habrahabr()
        update.message.reply_text(habr.get_habr_news(10))

    def var9(self, bot, update):
        var9 = Var9()
        update.message.reply_text(var9.get_sweet_word())

    def echo(self, bot, update):
        update.message.reply_text('Bot understand only commands!!!')

    def error(self, bot, update, error):
        self.logger.warn('Update "%s" caused error "%s"' % (update, error))

    def __init_logger(self):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def __init__(self):
        self.__init_logger()
        self.list_commands = ['help', 'weather', 'habr', 'news', 'var9']
        # Create the EventHandler and pass it your bot's token.
        updater = Updater('298011115:AAG0BDx80tIVOuOr8SiWrBSf538xaJzygjs')

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler(self.list_commands[0], self.help))
        dp.add_handler(CommandHandler(self.list_commands[1], self.weather))
        dp.add_handler(CommandHandler(self.list_commands[2], self.news))
        dp.add_handler(CommandHandler(self.list_commands[3], self.habrahabr))
        dp.add_handler(CommandHandler(self.list_commands[4], self.var9))
        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, self.echo))
        # on error
        dp.add_error_handler(self.error)


        # Start the Bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        #updater.idle()


