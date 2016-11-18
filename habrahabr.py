#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser
import ssl
from speech import Speech
# https://habrahabr.ru/rss/hubs/all/


class Habrahabr(object):
    def get_habr_news(self, max_value=10):
        ssl._create_default_https_context = ssl._create_unverified_context
        data = feedparser.parse('https://habrahabr.ru/rss/interesting/')
        habr_news_str = 'Новости: '
        counter = 1
        for e in data.entries:
            if counter - 1 == max_value:
                break
            habr_news_str += str(counter) + '. ' + e.title + ' из категории: ' + e.category + '.'
            counter += 1
        return habr_news_str

    def say_habr_news(self, max_value=10):
        habr_string = self.get_habr_news(max_value)
        speech = Speech()
        speech.say_text(habr_string)