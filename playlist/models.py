#coding:utf-8
from django.db import models

# Create your models here.

class upload_file(models.Model):
    filename=models.CharField('文件名',max_length=255)
    filepath=models.CharField('文件路径',max_length=255,null=True,blank=True)
    createtime=models.CharField('文件上传时间',max_length=255,null=True,blank=True)

class liveplaygroup(models.Model):
    livegroupname=models.CharField('播放组名称',max_length=50,null=True,blank=True)
    livegroupid=models.CharField('播放组ID',max_length=20,unique=True)
    livegroupdesc=models.CharField('播放组描述',max_length=255,null=True,blank=True)
    liverelate_id=models.TextField('关联的节目ID',max_length=1000,default="")

class liveplaygroup_adv(models.Model):
    livegroupid=models.ForeignKey(liveplaygroup, related_name='live_adv')
    channelid=models.CharField('频道ID',max_length=20,null=True,blank=True)
    advurl=models.CharField('广告图片下载地址',max_length=255,default="")
    advstate=models.CharField('启用状态',max_length=20,default=1)

class liveplaylist(models.Model):
    channelid=models.CharField('频道ID',max_length=20,null=True,blank=True)
    playaddress=models.CharField('播放地址',max_length=255,null=True,blank=True)
    classname=models.CharField('分类名称',max_length=255,null=True,blank=True)
    playname=models.CharField('节目名称',max_length=255,unique=True)
    mstatus=models.CharField('维护状态',max_length=20,default=1)
    picurl=models.CharField('维护图片下载地址',max_length=255,default="")

