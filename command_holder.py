#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weather import Weather
from telegram_bot import Telegram


class CommandHolder(object):
    def __init__(self):
        #telegram = Telegram()
        weather = Weather()
        self.commands = {
            'погода': weather.say_weather()
        }
        #self.telegram_commands = {
        #    'погода': telegram.say_text(weather.get_weather())
        #}

    def run_command(self, command_string, telegram=True):
        self.commands[command_string]


    def get_command_list(self):
        return self.command_list