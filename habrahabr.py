#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
from speech import Speech
# https://habrahabr.ru/rss/hubs/all/


class Habrahabr(object):
    def get_habr_news(self, max_value=10):
        data = feedparser.parse('https://habrahabr.ru/rss/interesting/')
        habr_news_str = 'Новости: '
        counter = 1
        for e in data.entries:
            if counter - 1 == max_value:
                break
            habr_news_str += str(counter) + '. ' + e.title.encode('utf-8') + ' из категории: ' + e.category.encode('utf-8') + '.'
            counter += 1
        #print(habr_news_str)
        return habr_news_str

    def say_habr_news(self, max_value=10):
        habr_string = self.get_habr_news(max_value)
        speech = Speech()
        speech.say_text(habr_string)