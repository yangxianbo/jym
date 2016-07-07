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
    url(r'^upadv$', 'up_adv', name='up_adv'),
    url(r'^disadv$', 'dis_adv', name='dis_adv'),
    url(r'^updateliveadv$', 'update_liveadv', name='update_liveadv'),
    url(r'^addlivegroup$', 'add_livegroup', name='add_livegroup'),
    url(r'^dellivegroup$', 'del_livegroup', name='del_livegroup'),
    url(r'^addliveall$', 'add_liveall', name='add_liveall'),
    url(r'^delliveall$', 'del_liveall', name='del_liveall'),
    url(r'^upmpic$', 'up_mpic', name='up_mpic'),
    url(r'^show_live_data/', 'show_live_data', name='show_live_data'),
    url(r'^dellive$', 'del_live', name='del_live'),
    url(r'^forcelive$', 'force_live', name='force_live'),
    url(r'^normallive$', 'normal_live', name='normal_live'),
    url(r'^relatelive$', 'relate_live', name='relate_live'),
    url(r'^relateliveall$', 'relate_liveall', name='relate_liveall'),
    url(r'^upfile$', 'up_file', name='up_file'),
    url(r'^uplogo$', 'up_logo', name='up_logo'),
    url(r'^delfile$', 'del_file', name='del_file'),
    url(r'^updatelivegroup$', 'update_livegroup', name='update_livegroup'),
    url(r'^liveadv/$', 'live_adv', {'template_name':'live/live_adv.html'}, name='live_adv'),
    url(r'^livegroupindex/$', 'livegroup_index', {'template_name':'live/livegroup_index.html'}, name='livegroup_index'),
    url(r'^liveindex/$', 'live_index', {'template_name':'live/live_index.html'}, name='live_index'),
    url(r'^liveall/$', 'live_all', {'template_name':'live/live_all.html'}, name='live_all'),
    url(r'^uplist/$', 'file_index', {'template_name':'upfile/playfile_index.html'}, name='file_index'),
)

