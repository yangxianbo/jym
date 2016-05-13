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
    url(r'^addpackage','add_package',name='add_package'),
    url(r'^delpackage','del_package',name='del_package'),
    url(r'^updatepackage','update_package',name='update_package'),
    url(r'^addrelate$', 'add_relate', name='add_relate'),
    url(r'^updaterelate$', 'update_relate', name='update_relate'),
    url(r'^delrelate$', 'del_relate', name='del_relate'),
    url(r'^addmachine$', 'add_machine', name='add_machine'),
    url(r'^updatemachine$', 'update_machine', name='update_machine'),
    url(r'^delmachine$', 'del_machine', name='del_machine'),
    url(r'^show_au_data/$', 'show_au_data', name='show_au_data'),
    url(r'^delauth$', 'del_auth', name='del_auth'),
    url(r'^delnew$', 'del_premachine', name='del_premachine'),
    url(r'^checkfile/$', 'check_file', {'template_name':'upfile/authsys_file.html'}, name='check_file'),
    url(r'^groupindex/$', 'authgroup_index', {'template_name':'authgroup/authgroup_index.html'}, name='authgroup_index'),
    url(r'^packageindex/$', 'package_index', {'template_name':'package/package_index.html'}, name='package_index'),
    url(r'^package/$', 'relate_index', {'template_name':'package/package_relateapp.html'}, name='relate_index'),
    url(r'^machineindex/$', 'machine_index', {'template_name':'authsys/machine_index.html'}, name='machine_index'),
    url(r'^authinfo/$', 'auth_info', {'template_name':'authsys/authinfo_index.html'}, name='auth_info'),
    url(r'^accesslog/$', 'access_log', {'template_name':'authsys/accesslog.html'}, name='access_log'),
    url(r'^managenew/$', 'pre_machine', {'template_name':'authsys/premachine.html'}, name='pre_machine'),
    url(r'^addnew/$', 'pre_authinfo', {'template_name':'authsys/preauth.html'}, name='pre_authinfo'),
)
