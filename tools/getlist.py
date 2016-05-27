#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-04-12 21:11:28
#FILENAME: getlist.py
#DESCRIPTION: 
#===============================================================

import base
from playlist.models import playgroup,liveplaylist
from authsys.models import authorization 
from utils import get_datatables_records,UnixTime,time_change_stime,timestamp,stime_change_time
from checkauth import Checkauth

def Getlist(mac,cpuid,appid,aucode,ip,localtime):
    check_status=Checkauth(mac,cpuid,appid,aucode,ip,localtime)
    if check_status == 0:
        play_dict={"live":[],"vod":[]}
        groupid=str(authorization.objects.get(mac__mac=mac,appid=appid).playid)
        groupquery=playgroup.objects.get(groupid=groupid)
        livegroupid=groupquery.livegroupid
        vodgroupid=groupquery.vodgroupid
        #查询直播列表
        live_group_query=liveplaygroup.objects.get(livegroupid=livegroupid)
        playidlist=live_group_query.liverelate_id.split(',')
        classall=liveplaylist.objects.filter(id__in=playidlist).values_list('classname').distinct()
        for classname in classall:
            class_dict={'classname':classname[0],'playlist':[]}
            liveall=liveplaylist.objects.filter(id__in=playidlist,classname=classname[0])
            for live in liveall:
                live_base={'address':live['playaddress'],'status':live['mstatus'],'pic':live['picurl'],'name':live['playname'],'id':live['channelid']}
                class_dict['playlist'].append(live_base)
            play_dict['live'].append(class_dict)
        #查询点播列表
        return play_dict
    else:
        play_dict={'code':check_status}
        return play_dict
                
