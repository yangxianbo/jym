#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-06-13 17:01:01
#FILENAME: playlist_templatetags.py
#DESCRIPTION: 
#===============================================================

import json,re, time, os, datetime,sys
from django import template
register = template.Library()

def check_name(cid,arg):
    c_dict=json.loads(arg)
    return c_dict[cid]

def cut(value):
    if value != None and value != "":
        if len(value) >= 20:
            cutstr=value[0:20]+"..."
        else:
            cutstr=value
    else:
        cutstr="无"
    return cutstr

register.filter(cut)
register.filter(check_name)

