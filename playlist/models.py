#coding:utf-8
from django.db import models

# Create your models here.

class upload_file(models.Model):
    filename=models.CharField('文件名',max_length=255)
    filepath=models.CharField('文件路径',max_length=255,null=True,blank=True)
    createtime=models.CharField('文件上传时间',max_length=255,null=True,blank=True)

class playgroup(models.Model):
    groupid=models.CharField('播放组ID',max_length=20,unique=True)
    livegroupid=models.CharField('直播播放组ID',max_length=20,null=True,blank=True)
    vodgroupid=models.CharField('点播播放组ID',max_length=20,null=True,blank=True)
    logourl=models.CharField('广告地址',max_length=255,default="")

class liveplaygroup(models.Model):
    livegroupname=models.CharField('播放组名称',max_length=50,null=True,blank=True)
    livegroupid=models.CharField('播放组ID',max_length=20,unique=True)
    livegroupdesc=models.CharField('播放组描述',max_length=255,null=True,blank=True)
    liverelate_id=models.TextField('关联的节目ID',max_length=1000,default="")

class liveplaylist(models.Model):
    channelid=models.CharField('频道ID',max_length=20,null=True,blank=True)
    playaddress=models.CharField('播放地址',max_length=255,null=True,blank=True)
    classname=models.CharField('分类名称',max_length=255,null=True,blank=True)
    playname=models.CharField('节目名称',max_length=255,unique=True)
    mstatus=models.CharField('维护状态',max_length=20,default=1)
    picurl=models.CharField('维护图片下载地址',max_length=255,default="")

