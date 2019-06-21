#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/20 14:25 
# @Author : wyao
# @File : decorate.py
import functools
from .exception import TypeNotExceptException


def str2dict(func):
    @functools.wraps(func)
    def wrapper(*argvs, **kwargvs):
        json_str = func(*argvs, **kwargvs)
        if isinstance(json_str, dict):return json_str
        if isinstance(json_str, str) is not True:
            raise TypeNotExceptException(json_str, 'str')
        try:
            dict_ret = eval(json_str)
        except SyntaxError:
            dict_ret = {'data': json_str}
        return dict_ret
    return wrapper