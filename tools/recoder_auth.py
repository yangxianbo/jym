#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-04-20 16:29:25
#FILENAME: recoder_auth.py
#DESCRIPTION: 
#===============================================================


import base
import os,sys
import xlrd
from authsys.models import upload_file,machine_info,authorization,group_info,package,package_relateapp
from aucode import Aucode
from utils import UnixTime,time_change_stime,timestamp,stime_change_time

class Recoder_auth():
    def __init__(self,filename):
        exname=os.path.splitext(filename)[-1]
        if exname != ".xls" and exname != ".xlsx":
            sys.exit("文件后缀错误")
        else:
            data = xlrd.open_workbook(filename)
            self.table = data.sheet_by_index(0)
            self.nrows = self.table.nrows

    def _checkmac(self,mac,cpuid,groupname):
        try:
            mkey=machine_info.objects.get(mac=mac)
            return mkey
        except machine_info.DoesNotExist:
            macnum=int(mac,16)
            mkey=machine_info.objects.create(mac=mac,cpuid=cpuid,groupname=groupname,macnum=macnum)
            mkey.save()
            return mkey

    def _getrelate(self,packageid):
        return_list=[]
        s_time=UnixTime()
        try:
            pkey=package.objects.get(packageid=packageid)
            autime=pkey.autime
            e_time=stime_change_time(time_change_stime(s_time)+(int(autime)*86400))
            relate_list=pkey.package_relate_app.all()
            for per in relate_list:
                appid=per.appid
                liveplayid=per.liveplayid
                vodplayid=per.vodplayid
                perlist=[appid,liveplayid,vodplayid,autime,s_time,e_time]
                return_list.append(perlist)
            return return_list
        except package.DoesNotExist:
            return return_list

    def _checkgroup(self,groupname):
        try:
            gkey=group_info.objects.get(groupname=groupname)
        except group_info.DoesNotExist:
            gkey=group_info.objects.create(groupname=groupname)
            gkey.save()

    def _addauth(self,mkey,appid,aucode,s_time,autime,e_time,liveplayid,vodplayid):
        try:
            akey=authorization.objects.filter(mac=mkey,appid=appid)
            if len(akey) == 0:
                akey=authorization.objects.create(mac=mkey,appid=appid,aucode=aucode,s_time=s_time,autime=autime,e_time=e_time,liveplayid=liveplayid,vodplayid=vodplayid,austate=0)
                akey.save()
                return 0
            else:
                base_autime=akey[0].autime
                base_stime=akey[0].s_time
                update_autime=int(base_autime)+int(autime)
                update_etime=stime_change_time(time_change_stime(base_stime)+((int(autime)+int(base_autime))*86400))
                akey.update(aucode=aucode,autime=update_autime,e_time=update_etime,liveplayid=liveplayid,vodplayid=vodplayid,austate=0)
                return 0
        except Exception,e:
            return -1

    def _add_motion(self,relate,mac,cpuid,groupname):
        #获得授权码
        appid=relate[0]
        liveplayid=relate[1]
        vodplayid=relate[1]
        autime=relate[2]
        s_time=relate[3]
        e_time=relate[4]
        enstr="%s+%s+%s"%(mac,cpuid,appid)
        encrypt=Aucode(enstr,0)
        aucode=encrypt.main()
        #执行授权
        mkey=self._checkmac(mac,cpuid,groupname)
        self._addauth(mkey,appid,aucode,s_time,autime,e_time,liveplayid,vodplayid)

    def _del_motion(self,mac):
        try:
            machine_info.objects.get(mac=mac).delete()
        except machine_info.DoesNotExist:
            pass

    def main(self):
        for xlsinfo in range(1,self.nrows):
            auth_list=self.table.row_values(xlsinfo)
            mac=auth_list[0]
            cpuid=auth_list[1]
            packageid=auth_list[2]
            groupname=auth_list[3]
            #查询组关联的APP与列表
            relate_list=self._getrelate(packageid)
            motion=auth_list[5]
            if int(motion) == 0:
                for relate in relate_list:
                    #如果不存在则创建组
                    self._checkgroup(groupname)
                    self._add_motion(relate,mac,cpuid,groupname)
                    return 0
            else:
                for relate in relate_list:
                    self._del_motion(mac)
                    return 0

