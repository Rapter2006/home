from random import choice
from speech import Speech

class Var9(object):
        def __init__(self):
            self.sweet_words = ['зайка', 'котик', 'рыбка', 'пууупсик', 'солнышко']

        def get_sweet_word(self):
            sweet_word = 'Даaaa, ' + choice(self.sweet_words)
            return sweet_word

        def say_sweet_word(self):
            speech = Speech()
            speech.say_text(self.get_sweet_word())
