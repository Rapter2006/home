#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
import urllib.request
import urllib.parse
import json
from speech import Speech


class Weather(object):
    def __complect_weather_string(self, dict_data):
        today_weather = dict_data['forecasts'][0]
        six_hours_weather = today_weather['hours'][1]
        midday_weather = today_weather['hours'][2]
        weather_str = 'В шесть утра была температура ' + str(six_hours_weather['temperature']['avg']) + \
                      ". Днем температура " + str(midday_weather['temperature']['avg']) + ', ветер ' + \
                      str(midday_weather['wind']['speed']['avg']) + ' метров в секунду.'
        return weather_str

    def get_weather(self):
        url = 'http://pogoda.ngs.ru/api/v1/forecasts/forecast?city=nsk'
        result = urllib.request.urlopen(url).read()
        decode_dict = json.loads(result.decode('utf-8'))
        return self.__complect_weather_string(decode_dict)

    def say_weather(self):
        weather_string = self.get_weather()
        speech = Speech()
        speech.say_text(weather_string)