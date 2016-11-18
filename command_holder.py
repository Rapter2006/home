from weather import Weather
from habrahabr import Habrahabr
from news import News
from var9 import Var9
from threading import Lock


class CommandHolder(object):
    def __init__(self):
        self.lock = Lock()
        self.weather = Weather()
        self.habr = Habrahabr()
        self.news = News()
        self.var9 = Var9()

    def run_command(self, command_string):
        with self.lock:
            if command_string == 'погода':
                self.weather.say_weather()
            if command_string == 'хабр':
                self.habr.say_habr_news(10)
            if command_string == 'новости':
                self.news.say_news(10)
            if command_string == 'варя':
                self.var9.say_sweet_word()


