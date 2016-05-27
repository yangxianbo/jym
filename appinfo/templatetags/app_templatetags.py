#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-05-18 14:52:32
#FILENAME: app_templatetags.py
#DESCRIPTION: 
#===============================================================


import json,re, time, os, datetime,sys
from django import template
register = template.Library()

def cut(value):
    if value != None and value != "":
        if len(value) >= 20:
            cutstr=value[0:20]+"... ..."
        else:
            cutstr=value
    else:
        cutstr="无"
    return cutstr

register.filter(cut)
