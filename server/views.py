#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/20 13:07 
# @Author : wyao
# @File : views.py
import json
from flask import Blueprint
from wise.wise import wise_client


view_page = Blueprint('view_page', __name__)


@view_page.route('/lamp1_change')
def lamp1_change():
    wise_client.lamp1_change()
    return json.dumps(wise_client.get_lamp_state())


@view_page.route('/lamp2_change')
def lamp2_change():
    wise_client.lamp2_change()
    return json.dumps(wise_client.get_lamp_state())


@view_page.route('/lamp_get')
def lamp_state():
    return json.dumps(wise_client.get_lamp_state())


@view_page.route('/ai_info')
def ai_info():
    return json.dumps(wise_client.get_ai_info())