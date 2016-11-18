#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from command_holder import CommandHolder

app = Flask(__name__)
command_holder = CommandHolder()

@app.route('/command', methods=['POST'])
def run_command():
    command_name = request.form['name']
    command_holder.run_command(command_name)
    return '', 200, {'ContentType': 'application/json'}

if __name__ == "__main__":
    app.run()