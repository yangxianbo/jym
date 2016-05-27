# -*- coding: utf-8 -*-
import json,re, time, os, datetime,sys
from django import template
register = template.Library()


def rrdtool_time(value):
    def UnixTime(day=0, FORMAT="%Y-%m-%d %H:%M:%S"):
        return time.strftime(FORMAT, time.localtime(time.time()-86400*day))
    text = ''
    if value == 'yesterday':
        text = 'start_time=%s&end_time=%s' % (UnixTime(2),UnixTime(1))
    elif value == 'today':
        text = 'start_time=%s&end_time=%s' % (UnixTime(1),UnixTime())
    elif value == 'week':
        text = 'start_time=%s&end_time=%s' % (UnixTime(7),UnixTime())
    elif value == '15day':
        text = 'start_time=%s&end_time=%s' % (UnixTime(15),UnixTime())
    elif value == 'month':
        text = 'start_time=%s&end_time=%s' % (UnixTime(30),UnixTime())
    elif value == 'years':
        text = 'start_time=%s&end_time=%s' % (UnixTime(360),UnixTime())
    else:
        pass
    return ('%s&t=%s') % (text,value)

def strf_time(value):
    return value.strftime('%Y-%m-%d %H:%M:%S')


register.filter(rrdtool_time)
register.filter(strf_time)
