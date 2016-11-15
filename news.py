#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib.request
import urllib.parse
import json

class News(object):
    def get_news(self):
        url = 'https://meduza.io/api/v3/search?chrono=news&page=0&per_page=10&locale=ru'
        result = urllib.request.urlopen(url).read()
        print(result.decode('unicode'))
        #decode_dict = json.loads(result.decode('utf-8'))
        #print(decode_dict)
