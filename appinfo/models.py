#coding:utf-8
from django.db import models

# Create your models here.
class appinfo(models.Model):
    appid=models.CharField('APPID',max_length=50,unique=True)
    appname=models.CharField('APP名称',max_length=50,null=True,blank=True)
    appdesc=models.CharField('描述',max_length=255,null=True,blank=True)
    appfolder=models.CharField('包名',max_length=255,null=True,blank=True)
    uptime=models.CharField('上传时间',max_length=255,null=True,blank=True)
    version=models.CharField('版本号',max_length=255,null=True,blank=True)
    downloadurl=models.CharField('下载地址',max_length=255,default="")
    appsize=models.CharField('大小',max_length=50,null=True,blank=True)
    upstate=models.CharField('更新状态',max_length=50,default=1)
    ticker=models.TextField('跑马灯',max_length=500,default="")
