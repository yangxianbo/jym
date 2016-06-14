#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-05-13 17:12:24
#FILENAME: dopreauth.py
#DESCRIPTION: 
#===============================================================


import base
from authsys.models import machine_info,authorization
from utils import UnixTime,time_change_stime,timestamp,stime_change_time

class Dopreauth():
    def __init__(self,mac,cpuid,appid,liveplayid,vodplayid,aucode,autime):
        self.mac=mac
        self.cpuid=cpuid
        self.appid=appid
        self.liveplayid=liveplayid
        self.vodplayid=vodplayid
        self.aucode=aucode
        self.autime=autime
        self.localtime=UnixTime()

    def _check_machine(self):
        if len(machine_info.objects.filter(mac=self.mac)) == 0:
            new=machine_info.objects.create(mac=self.mac,
                                        cpuid=self.cpuid,
                                        macnum=int(self.mac,16),
                                        agency='baseagency',
            )
            new.save()
            mkey=machine_info.objects.get(mac=self.mac)
            return mkey
        else:
            mkey=machine_info.objects.get(mac=self.mac)
            return mkey

    def _create_auth(self,mkey):
        e_time=stime_change_time(time_change_stime(self.localtime)+(int(self.autime)*86400))
        new=authorization.objects.create(mac=mkey,
                                    appid=self.appid,
                                    liveplayid=self.liveplayid,
                                    vodplayid=self.vodplayid,
                                    aucode=self.aucode,
                                    autime=self.autime,
                                    s_time=self.localtime,
                                    e_time=e_time,
                                    austate=0,
        )
        new.save()

    def main(self):
        mkey=self._check_machine()
        self._create_auth(mkey)
        return 0



