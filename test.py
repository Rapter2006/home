#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weather import Weather
from speech import Speech
from command_holder import CommandHolder
from news import News
# w = Weather()
# weather = w.get_weather()
# s = Speech()
# s.say_text(weather)
#
# c = CommandHolder()
# c.run_command('погода')
n = News()
n.get_news()