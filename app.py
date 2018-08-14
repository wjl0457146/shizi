#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

from flask import Flask

from randomchinese import ChooseZi

app = Flask(__name__)


@app.route('/')
def hello_world():
    # line1 = ''
    # import random
    # result = random.sample(['日', '月', '天', '地', '一'], 3)
    # print result
    # for line in result:
    #     line1 += line
    # return line1
    return ChooseZi()



if __name__ == '__main__':
    app.run()

