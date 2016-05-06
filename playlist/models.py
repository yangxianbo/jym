#coding:utf-8
from django.db import models

# Create your models here.

class upload_file(models.Model):
    filename=models.CharField('文件名',max_length=255)
    filepath=models.CharField('文件路径',max_length=255)
    playtype=models.CharField('播放类型',max_length=20)
    filestate=models.CharField('文件处理状态',max_length=20,default=1)
    createtime=models.CharField('文件上传时间',max_length=255,null=True,blank=True)
    dotime=models.CharField('文件处理时间',max_length=255,null=True,blank=True)

class playgroup(models.Model):
    groupname=models.CharField('播放组名称',max_length=50)
    groupid=models.CharField('播放组ID',max_length=20,unique=True)
    groupdesc=models.CharField('播放组描述',max_length=255,null=True,blank=True)

class liveplaylist(models.Model):
    groupid=models.CharField('播放组ID',max_length=20)
    playaddress=models.CharField('播放地址',max_length=255)
    classname=models.CharField('分类名称',max_length=255,null=True,blank=True)
    playname=models.CharField('节目名称',max_length=255,null=True,blank=True)
    playid=models.CharField('节目ID',max_length=20,unique=True)

