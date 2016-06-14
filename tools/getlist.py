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

def Getlist(mac,cpuid,appid,aucode,ip,localtime):
    check_status=Checkauth(mac,cpuid,appid,aucode,ip,localtime)
    play_list=[]
    if check_status == 0:
        mkey=authorization.objects.get(mac__mac=mac,appid=appid)
        livegroupid=mkey.liveplayid
        #查询直播列表
        live_group_query=liveplaygroup.objects.get(livegroupid=livegroupid)
        playidlist=live_group_query.liverelate_id.split(',')
        #查询广告
        advlist=liveplaygroup_adv.objects.filter(livegroupid=live_group_query).values_list('channelid','advstate','advurl')
        adv_dict={}
        for adv in advlist:
            adv_dict[adv[0]]=[adv[1],adv[2]]
        try:
            classall=liveplaylist.objects.filter(id__in=playidlist).values_list('classname').distinct()
            for classname in classall:
                class_dict={'classname':classname[0],'playlist':[]}
                liveall=liveplaylist.objects.filter(id__in=playidlist,classname=classname[0]).order_by('id').values()
                for live in liveall:
                    liveadvurl=adv_dict[str(live['id'])][1]
                    liveadvstate=adv_dict[str(live['id'])][0]
                    live_base={'address':live['playaddress'],'status':live['mstatus'],'pic':live['picurl'],'name':live['playname'],'id':live['channelid'],'advurl':liveadvurl,'advstate':liveadvstate}
                    class_dict['playlist'].append(live_base)
                play_list.append(class_dict)
        except ValueError:
                pass
        return play_list
    else:
        play_list.append({'code':check_status})
        return play_list
                
