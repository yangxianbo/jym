#coding:utf-8
from django.conf.urls import patterns, url, include

urlpatterns = patterns('account.views',
    url(r'^user_index/$', 'user_index', {'template_name':'user/user_index.html'}, name='user_index'),
#    url(r'^add_user_index/$', 'add_user_index', name='add_user_index'),
    url(r'^show_md_data/$', 'show_md_data', name='show_md_data'),
    url(r'^del_user_index/$', 'del_user_index', name='del_user_index'),

    url(r'^group_index/$', 'group_index', {'template_name':'group/group_index.html'}, name='group_index'),
    url(r'^delete_count/$', 'delete_count', name='delete_count'),
)

urlpatterns += patterns('account.user_login',
    url(r'^login/$', 'Login', {'template_name':'login/login.html'}, name='Login'),
    url(r'^Logout/$', 'Logout', name='Logout'),
    url(r'^change_password/$', 'change_password', name='change_password'),
)

