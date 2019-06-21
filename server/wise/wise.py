#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/20 11:05 
# @Author : wyao
# @File : wise.py.py
from .wise_request.wise_request import WiseRequest
from . import config


class Wise:

    def __init__(self, ip, account: str=config.ACCOUNT, password: str=config.PASSWORD):
        self.request_client = WiseRequest(ip, account, password)

    def _request(self, request_argvs: dict):
        return self.request_client.request(request_argvs['url'], request_argvs['data'], request_argvs['method'])

    def lamp1_on(self):
        return self._request(config.LAMP1_ON)

    def lamp1_off(self):
        return self._request(config.LAMP1_OFF)

    def lamp2_on(self):
        return self._request(config.LAMP2_ON)

    def lamp2_off(self):
        return self._request(config.LAMP2_OFF)

    def get_lamp_state(self):
        return self._request(config.LAMP_STATUS)

    def islamp1on(self):
        return True if self.get_lamp_state()['DOVal'][0]['Val'] == 1 else False

    def islamp2on(self):
        return True if self.get_lamp_state()['DOVal'][1]['Val'] == 1 else False

    def lamp1_change(self):
        self.lamp1_off() if self.islamp1on() else self.lamp1_on()

    def lamp2_change(self):
        self.lamp2_off() if self.islamp2on() else self.lamp2_on()

    def get_ai_info(self):
        return self._request(config.AI_INFO)


wise_client = Wise(config.IP)