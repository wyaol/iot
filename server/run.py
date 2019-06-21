#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/20 9:42 
# @Author : wyao
# @File : run.py
from flask import Flask, render_template
import flask_cors
from views import view_page

app = Flask(__name__)
app.register_blueprint(view_page)
flask_cors.CORS(app, supperts_credentials=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')