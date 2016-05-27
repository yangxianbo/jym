#coding:utf-8
from django.db import models

# Create your models here.
class upload_file(models.Model):
    filename=models.CharField('文件名',max_length=255)
    filepath=models.CharField('文件路径',max_length=255)
    status=models.CharField('文件处理状态',max_length=20,default=1)
    createtime=models.CharField('文件上传时间',max_length=255,null=True,blank=True)
    dotime=models.CharField('文件处理时间',max_length=255,null=True,blank=True)

class group_info(models.Model):
    agency=models.CharField('代理商',max_length=255,unique=True,default="baseagency")
    groupdesc=models.CharField('描述',max_length=255,null=True,blank=True)
    tickerid=models.CharField('跑马灯ID',max_length=20,null=True,blank=True)
    blacklocation=models.CharField('区域限制',max_length=255,default="")
    def __unicode__(self):
        return self.agency

class ticker_info(models.Model):
    ticker=models.TextField('跑马灯',max_length=500,null=True,blank=True)
    tickerid=models.CharField('跑马灯ID',max_length=20,unique=True)

class package(models.Model):
    packageid=models.CharField('套餐ID',max_length=20,unique=True)
    packagename=models.CharField('套餐名称',max_length=20,null=True,blank=True)
    autime=models.CharField('授权时长',max_length=50,null=True,blank=True)
    spare=models.CharField('备用字段',max_length=255,null=True,blank=True)

class package_relateapp(models.Model):
    packageid=models.ForeignKey(package, related_name='package_relate_app')
    appid=models.CharField('APPID',max_length=20,null=True,blank=True)
    playid=models.CharField('关联列表',max_length=255,null=True,blank=True)

class machine_info(models.Model):
    agency=models.CharField('代理商',max_length=255,default="baseagency")
    mac=models.CharField('MAC码',max_length=25,unique=True)
    macnum=models.CharField('数字码',max_length=25,null=True,blank=True)
    cpuid=models.CharField('CPUID',max_length=255,default="ffffffff-d4bd-1afb-3ba9-893c0033c587")
    blacklocation=models.CharField('区域限制',max_length=255,default="")
    def __unicode__(self):
        return self.mac

class authorization(models.Model):
    mac=models.ForeignKey(machine_info, related_name='app_auth_info')
    appid=models.CharField('APPID',max_length=20,null=True,blank=True)
    aucode=models.CharField('授权码',max_length=255)
    s_time=models.CharField('授权开始时间',max_length=255,default="2016-04-01 00:00:00")
    autime=models.CharField('授权时长',max_length=50,null=True,blank=True)
    e_time=models.CharField('授权结束时间',max_length=255,null=True,blank=True)
    austate=models.CharField('授权状态',max_length=20,default=1)
    playid=models.CharField('关联列表',max_length=255,null=True,blank=True)
    dostate=models.CharField('鉴权状态',max_length=20,default=1)
    dotime=models.CharField('鉴权时间',max_length=255,default="2016-04-01 00:00:00")
    spare=models.CharField('备用字段',max_length=255,null=True,blank=True)
    def __unicode__(self):
        return self.aucode

class premachine_info(models.Model):
    mac=models.CharField('MAC码',max_length=25,unique=True)
    macnum=models.CharField('数字码',max_length=25,null=True,blank=True)
    cpuid=models.CharField('CPUID',max_length=255,default="ffffffff-d4bd-1afb-3ba9-893c0033c587")
    spare=models.CharField('备用字段',max_length=255,null=True,blank=True)
    def __unicode__(self):
        return self.mac

class preauthorization(models.Model):
    mac=models.ForeignKey(premachine_info, related_name='app_pre_info')
    cpuid=models.CharField('CPUID',max_length=255,default="ffffffff-d4bd-1afb-3ba9-893c0033c587")
    appid=models.CharField('APPID',max_length=20,null=True,blank=True)
    ipaddress=models.GenericIPAddressField('访问的IP',null=True,blank=True)
    register_time=models.CharField('请求时间',max_length=255)
    prestate=models.CharField('处理状态',max_length=20,default=1)
    spare=models.CharField('备用字段',max_length=255,null=True,blank=True)

class accesslog(models.Model):
    mac=models.ForeignKey(authorization, related_name='access_log')
    cpuid=models.CharField('CPUID',max_length=255,default="ffffffff-d4bd-1afb-3ba9-893c0033c587")
    appid=models.CharField('APPID',max_length=20,null=True,blank=True)
    ipaddress=models.GenericIPAddressField('访问的IP',null=True,blank=True)
    aucode=models.CharField('授权码',max_length=255)
    a_time=models.DateTimeField('鉴权时间',auto_now_add=True)
    dostate=models.CharField('鉴权状态',max_length=20)
    spare=models.CharField('备用字段',max_length=255,null=True,blank=True)
    def __unicode__(self):
        return self.aucode
