#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class Telegram(object):
    def say_text(self, bot, update):

        update.message.reply_text(update.message.text)

    def __init__(self):
        token = '298011115:AAG0BDx80tIVOuOr8SiWrBSf538xaJzygjs'
        # Create the EventHandler and pass it your bot's token.
        updater = Updater(token)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, self.say_text))

        # Start the Bot
        updater.start_polling()

        updater.idle()


