#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-04-12 21:11:28
#FILENAME: getlist.py
#DESCRIPTION: 
#===============================================================

import base
from playlist.models import liveplaylist,liveplaygroup,liveplaygroup_adv
from authsys.models import authorization 
from utils import get_datatables_records,UnixTime,time_change_stime,timestamp,stime_change_time
from checkauth import Checkauth

def get_classinfo(classname,playidlist,live_group_query):
    #查询广告
    advlist=liveplaygroup_adv.objects.filter(livegroupid=live_group_query).values_list('channelid','advstate','advurl')
    adv_dict={}
    for adv in advlist:
        adv_dict[adv[0]]=[adv[1],adv[2]]
    class_dict={'classname':classname,'playlist':[]}
    try:
        liveall=liveplaylist.objects.filter(id__in=playidlist).order_by('id').values()
        for live in liveall:
            liveadvurl=adv_dict[str(live['id'])][1]
            liveadvstate=adv_dict[str(live['id'])][0]
            live_base={'address':live['playaddress'],'status':live['mstatus'],'pic':live['picurl'],'name':live['playname'],'id':live['channelid'],'advurl':liveadvurl,'advstate':liveadvstate}
            class_dict['playlist'].append(live_base)
    except ValueError:
            pass
    return class_dict

def Getlist(mac,cpuid,appid,aucode,ip,localtime):
    check_status=Checkauth(mac,cpuid,appid,aucode,ip,localtime)
    play_list=[]
    if check_status == 0:
        mkey=authorization.objects.get(mac__mac=mac,appid=appid)
        livegroupid=mkey.liveplayid
        #查询直播列表
        live_query=liveall.objects.get(pk=livegroupid)
        live_group_list=live_query.liverelate_group.split(',')
        for live_group in live_group_list:
            live_group_query=liveplaygroup.objects.get(pk=live_group)
            playidlist=live_group_query.liverelate_id.split(',')
            live_group_name=live_group_query.livegroupname
            class_dict=get_classinfo(live_group_name,playidlist,live_group_query)
            play_list.append(class_dict)
        return play_list
    else:
        play_list.append({'code':check_status})
        return play_list
                
