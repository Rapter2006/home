#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import urllib
import subprocess
import os


class Speech(object):
    """
       Отвечает за все операции, производимые с голосом
    """

    def __init__(self):
        self._audio_format = 'mp3'
        self._speaker_voice = 'omazh'
        self._key = '4e8ef9aa-5135-4753-89e5-33cfea6d51c4'

    """
    file=<название файла для сохранения> - по умолчанию "voice.mp3"
    text=<текст для генерации> - "гот%2bов"
    format=<формат аудио файла> - "mp3", "wav"
    lang=<язык> - "ru‑RU"
    speaker=<голос> - female: jane, omazh; male: zahar, ermil
    key=<API‑ключ>
    [emotion=<окраска голоса>] - neutral(нейтральный), evil (злой), mixed (переменная окраска)
    [drunk=<окраска голоса>] - true, false
    [ill=<окраска голоса>] - true, false
    [robot=<окраска голоса>] - true, false

    Вернет: имя файла, в котором будет содержаться аудио формат текста
    """

    def __text_to_audio_file(self, text, audio_format, speaker, key, file='voice.mp3', **a):
        url = 'https://tts.voicetech.yandex.net/generate?' \
              'text={text}&' \
              'format={audio_format}&' \
              'lang=ru-RU&' \
              'speaker={speaker}&' \
              'key={key}&'

        text = urllib.parse.quote(text)
        url = url.format(
            text=text,
            audio_format=audio_format,
            speaker=speaker,
            key=key
        )
        if a:
            url += urllib.parse.urlencode(a)

        urllib.request.urlretrieve(url, file)
        return (os.path.dirname(__file__)) + '/' + file

    # Проиграет аудиофайл с помощью mpg123
    def play_audio(self, path_to_audio_file):
        subprocess.Popen(['mpg123', '-q', path_to_audio_file]).wait()

    # Переведет текст в аудиофайл, затем проиграет его
    def say_text(self, text_to_say):
        # получим файл
        file_name = self.__text_to_audio_file(text_to_say, self._audio_format, self._speaker_voice, self._key)
        # проиграем его
        self.play_audio(file_name)