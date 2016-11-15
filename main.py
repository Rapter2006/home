#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from speech import Speech
app = Flask(__name__)

@app.route("/")
def hello():
    s = Speech('record.mp3')
    s.get_mp3_file_from_text('Привет')
    return "Hello World!"

if __name__ == "__main__":
    app.run()