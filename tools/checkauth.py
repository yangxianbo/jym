#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-04-13 00:40:14
#FILENAME: checkauth.py
#DESCRIPTION: 
#===============================================================
import base
from authsys.models import authorization,accesslog
from tools.aucode import Aucode

def check_location(ip):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('select location from iplocation where ip_end > inet_aton(%s) limit 1'%ip)
    location=cursor.fetchone()[0]
    cursor.close()
    return location

def Checkauth(mac,cpuid,appid,aucode,ip,localtime):
    try:
        mkey=machine_info.objects.get(mac=mac)
        locationlist=mkey.blacklocation.split(',')
        location=check_location(ip)
        if location not in locationlist:
            akey=authorization.objects.get(mac=mkey,appid=appid)
            if akey.aucode != aucode or int(akey.austate) != 0:
                akey.dostate=1
                akey.save()
                return -9000
            else:
                decode=Aucode(aucode,1)
                decode_info=decode.main()
                if isinstance(decode_info,list):
                    if cpuid not in decode_info and mac not in decode_info and appid not in  decode_info:
                        akey.dostate=1
                        akey.dotime=localtime
                        akey.save()
                        create_log=accesslog.objects.create(mac=akey,cpuid=cpuid,appid=appid,ipaddress=ip,dostate=1,aucode=aucode)
                        create_log.save()
                        return -9000
                    else:
                        akey.dostate=0
                        akey.dotime=localtime
                        akey.save()
                        create_log=accesslog.objects.create(mac=akey,cpuid=cpuid,appid=appid,ipaddress=ip,dostate=0,aucode=aucode)
                        create_log.save()
                        return 0
        else:
            return -8000
    except authorization.DoesNotExist:
        return -9004

