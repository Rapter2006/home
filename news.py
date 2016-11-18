#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib.request
import urllib.parse
import json
import zlib
import ssl
from speech import Speech


class News(object):
    def say_news(self, max_value=10):
        news_string = self.get_news(max_value)
        speech = Speech()
        speech.say_text(news_string)

    def get_news(self, max_value=10):
        ssl._create_default_https_context = ssl._create_unverified_context
        url = 'https://meduza.io/api/v3/search?chrono=news&page=0&per_page=10&locale=ru'
        result = urllib.request.urlopen(url).read()
        decompressed_data = zlib.decompress(result, 16+zlib.MAX_WBITS).decode('utf-8')
        decode_dict = json.loads(decompressed_data)
        return self.__complect_news_string(decode_dict, max_value)

    def __complect_news_string(self, dict_data, max_value):
        news_string = 'Новости: '
        counter = 1
        for value in dict_data['documents'].values():
            if counter - 1 == max_value:
                break
            news_string += str(counter) + '. ' + value['title'] + '. '
            counter += 1
        return news_string

