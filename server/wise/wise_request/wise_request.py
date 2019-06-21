#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/20 11:09 
# @Author : wyao
# @File : wise_request.py
import requests
import base64
import json
from .tools.decorate import str2dict
from . import config


class WiseRequest:

    def __init__(self, ip, account, password):
        self.sess = requests.session()
        self.headers = config.HEADERS
        self.ip = ip
        self.account = account
        self.password = password
        self.init_headers()

    def get_auth(self):
        step1 = '%s:%s'%(self.account, self.password)
        step2 = base64.b64encode(step1.encode('utf-8'))
        return 'Basic %s'%(str(step2, encoding='utf-8'))

    def init_headers(self):
        self.headers['Authorization'] = self.get_auth()

    @str2dict
    def request(self, url, data, method='patch'):
        data = json.dumps(data)
        if method == 'patch':
            json_str = requests.patch(url%self.ip, data=data, headers=self.headers)
        elif method == 'get':
            json_str = requests.get(url%self.ip, data=data, headers=self.headers)
        elif method == 'post':
            json_str = requests.post(url % self.ip, data=data, headers=self.headers)
        else:
            return {'success': False, 'msg': 'method is not define, method: %s'%(method)}
        return json_str.text