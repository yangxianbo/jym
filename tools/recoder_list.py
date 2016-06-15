#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-05-20 16:24:36
#FILENAME: recoder_list.py
#DESCRIPTION: 
#===============================================================


import base
import os,sys
import xlrd
from playlist.models import *
from utils import UnixTime

class Recoder_list():
    def __init__(self,filename):
        exname=os.path.splitext(filename)[-1]
        if exname != ".xls" and exname != ".xlsx":
            sys.exit("文件后缀错误")
        else:
            data = xlrd.open_workbook(filename)
            self.table = data.sheet_by_index(0)
            self.nrows = self.table.nrows

    def _add_live(self,classname,channelid,playname,playaddress):
        if len(liveplaylist.objects.filter(playaddress=playaddress,playname=playname)) == 0:
            new=liveplaylist.objects.create(channelid=channelid,playname=playname,classname=classname,playaddress=playaddress)
            new.save()
        else:
            pass

    def main(self):
        for xlsinfo in range(1,self.nrows):
            playlist=self.table.row_values(xlsinfo)
            playtype=playlist[0]
            if playtype == 'live':
                classname=playlist[1]
                channelid=int(playlist[2])
                playname=playlist[3]
                playaddress=playlist[4]
                self._add_live(classname,channelid,playname,playaddress)
            else:
                pass
