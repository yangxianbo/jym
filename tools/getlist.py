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
        #查询直播列表
        classquery=liveplaylist.objects.filter(groupid=groupid).values('classname').distinct()
        if len(classquery) != 0:
            for classname in classquery:
                class_dict={'classname':classname['classname'],'playlist':[]}
                listquery=liveplaylist.objects.filter(groupid=groupid,classname=classname['classname']).values()
                for playinfo in listquery:
                    live_base={}
                    live_base['name']=playinfo['playname']
                    live_base['id']=playinfo['playid']
                    live_base['address']=playinfo['playaddress']
                    class_dict['playlist'].append(live_base)
                play_dict['live'].append(class_dict)
            return play_dict
        #查询点播列表
        else:
            return play_dict
    else:
        return check_status
                
