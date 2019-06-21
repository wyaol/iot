#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/20 11:36 
# @Author : wyao
# @File : config.py
import copy


IP = '192.168.43.71'
ACCOUNT = 'root'
PASSWORD = '00000000'

LAMP1_ON = {
    'url': 'http://%s/do_value/slot_0',
    'method': 'patch',
    'data': {
        'DOVal': [{
            'Ch': 0,
            'Val': 1
        }]
    }
}

LAMP1_OFF = copy.deepcopy(LAMP1_ON)
LAMP1_OFF['data']['DOVal'][0]['Val'] = 0

LAMP2_ON = copy.deepcopy(LAMP1_ON)
LAMP2_ON['data']['DOVal'][0]['Ch'] = 1

LAMP2_OFF = copy.deepcopy(LAMP1_OFF)
LAMP2_OFF['data']['DOVal'][0]['Ch'] = 1

LAMP_STATUS = copy.deepcopy(LAMP1_ON)
LAMP_STATUS['method'] = 'get'
LAMP_STATUS['data'] = None

AI_INFO =  {
    'url': 'http://%s/ai_value/slot_0',
    'method': 'get',
    'data': None
}