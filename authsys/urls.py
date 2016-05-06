#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-04-11 15:16:34
#FILENAME: urls.py
#DESCRIPTION: 
#===============================================================


from django.conf.urls import include, url, patterns

urlpatterns = patterns('authsys.views',
    url(r'^getauth$', 'manage_auth', name='manage_auth'),
    url(r'^checkauth$', 'check_auth', name='check_auth'),
    url(r'^upfile$', 'up_file', name='up_file'),
    url(r'^delfile$', 'del_file', name='del_file'),
    url(r'^dofile$', 'do_file', name='do_file'),
    url(r'^addgroup$', 'add_group', name='add_group'),
    url(r'^delgroup$', 'del_group', name='del_group'),
    url(r'^updategroup$', 'update_group', name='update_group'),
    url(r'^addrelate$', 'add_relate', name='add_relate'),
    url(r'^updaterelate$', 'update_relate', name='update_relate'),
    url(r'^delrelate$', 'del_relate', name='del_relate'),
    url(r'^checkfile/$', 'check_file', {'template_name':'upfile/authsys_file.html'}, name='check_file'),
    url(r'^groupindex/$', 'authgroup_index', {'template_name':'authgroup/authgroup_index.html'}, name='authgroup_index'),
    url(r'^relateapp/$', 'relate_app', {'template_name':'package/package_relateapp.html'}, name='relate_app'),
)
