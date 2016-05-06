# -*- coding: utf-8 -*-
import re, time, os, datetime
from django import template
from account.models import UserProfile, UserGroup
from django.contrib.auth.models import User
register = template.Library()

def fq_member_change(idlist):
    queryset=UserProfile.objects.filter(user__id__in=idlist.split(","))
    member_all_cn=[]
    for row in queryset:
        member_all_cn.append(row.user.first_name)
    return ','.join(member_all_cn)


def fq_name_change(idlist):
    queryset=UserGroup.objects.filter(id__in=idlist.split(","))
    gname_all_cn=[]
    for row in queryset:
        gname_all_cn.append(row.gname)
    return ','.join(gname_all_cn)


def time_difference(time_tmp):
    print time_tmp
    start = int(time.mktime(time.strptime(time_tmp,'%Y-%m-%d %H:%M:%S')))
    d1 = datetime.datetime.fromtimestamp(int(time.time()))
    d2 = datetime.datetime.fromtimestamp(int(start))
    hour = (d1-d2).seconds  / 3600
    minutes = ((d1-d2).seconds - (3600 * hour)) / 60

    if (d1-d2).days != 0 and (d1-d2).seconds / (60 * 60) != 0:
        return ('%s天%s小时%s分钟') % ((d1-d2).days,(d1-d2).seconds / (60 * 60),minutes)
    else:
        if (d1-d2).seconds / (60 * 60) != 0:
            return ('%s小时%s分钟') % ((d1-d2).seconds / (60 * 60),minutes)
        else:
            return ('%s分钟') % (minutes)

register.filter(time_difference)
register.filter(fq_member_change)
register.filter(fq_name_change)
