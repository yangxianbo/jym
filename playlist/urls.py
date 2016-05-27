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
    url(r'^addgroup$', 'add_group', name='add_group'),
    url(r'^delgroup$', 'del_group', name='del_group'),
    url(r'^updategroup$', 'update_group', name='update_group'),
    url(r'^addlivegroup$', 'add_livegroup', name='add_livegroup'),
    url(r'^dellivegroup$', 'del_livegroup', name='del_livegroup'),
    url(r'^upmpic$', 'up_mpic', name='up_mpic'),
    url(r'^show_live_data/', 'show_live_data', name='show_live_data'),
    url(r'^dellive$', 'del_live', name='del_live'),
    url(r'^forcelive$', 'force_live', name='force_live'),
    url(r'^normallive$', 'normal_live', name='normal_live'),
    url(r'^relatelive$', 'relate_live', name='relate_live'),
    url(r'^upfile$', 'up_file', name='up_file'),
    url(r'^uplogo$', 'up_logo', name='up_logo'),
    url(r'^delfile$', 'del_file', name='del_file'),
    url(r'^updatelivegroup$', 'update_livegroup', name='update_livegroup'),
    url(r'^groupindex/$', 'group_index', {'template_name':'group/playgroup_index.html'}, name='group_index'),
    url(r'^livegroupindex/$', 'livegroup_index', {'template_name':'live/livegroup_index.html'}, name='livegroup_index'),
    url(r'^liveindex/$', 'live_index', {'template_name':'live/live_index.html'}, name='live_index'),
    url(r'^uplist/$', 'file_index', {'template_name':'upfile/playfile_index.html'}, name='file_index'),
)

