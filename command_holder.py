#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weather import Weather
from habrahabr import Habrahabr
from news import News

class CommandHolder(object):
    def __init__(self):
        weather = Weather()
        habr = Habrahabr()
        news = News()
        self.commands = {
            'погода': weather.say_weather(),
            'хабр': habr.say_habr_news(10),
            'новости': news.say_news(10),
        }

    def run_command(self, command_string, telegram=True):
        self.commands[command_string]

    def get_command_list(self):
        return self.command_list


