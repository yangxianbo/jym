#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-05-17 10:50:09
#FILENAME: urls.py
#DESCRIPTION: 
#===============================================================


from django.conf.urls import include, url, patterns
urlpatterns = patterns('appinfo.views',
    url(r'^delapk$', 'del_file', name='del_file'),
    url(r'^forceapk$', 'force_apk', name='force_apk'),
    url(r'^normalapk$', 'normal_apk', name='normal_apk'),
    url(r'^upapk$', 'up_file', name='up_file'),
    url(r'^showinfo$', 'quest_app', name='quest_app'),
    url(r'^show_app_data/$', 'show_app_data', name='show_app_data'),
    url(r'^appindex/$', 'appinfo_index', {'template_name':'app/appinfo_index.html'}, name='appinfo_index'),
    
)

