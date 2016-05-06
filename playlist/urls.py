#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-04-13 09:08:24
#FILENAME: urls.py
#DESCRIPTION: 
#===============================================================


from django.conf.urls import include, url, patterns

urlpatterns = patterns('playlist.views',
    url(r'^getlist$', 'get_playlist', name='get_playlist'),
)

