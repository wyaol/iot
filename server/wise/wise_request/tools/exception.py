#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/20 14:25 
# @Author : wyao
# @File : exception.py
class TypeNotExceptException(Exception):

    def __init__(self, argv, type: str):
        self.argv = argv
        self.type = type

    def __str__(self):
        return 'the type of the argv is %s, but actual type is %s'%(type(self.argv), self.type)