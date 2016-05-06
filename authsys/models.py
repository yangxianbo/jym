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
    groupname=models.CharField('组名',max_length=255,unique=True,default="basegroup")
    groupdesc=models.CharField('描述',max_length=255,null=True,blank=True)
    agency=models.CharField('代理商',max_length=255,null=True,blank=True)
    def __unicode__(self):
        return self.groupname

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
    groupname=models.CharField('组名',max_length=255,default="basegroup")
    mac=models.CharField('MAC码',max_length=25,unique=True)
    macnum=models.CharField('数字码',max_length=25,null=True,blank=True)
    cpuid=models.CharField('CPUID',max_length=255,default="ffffffff-d4bd-1afb-3ba9-893c0033c587")
    spare=models.CharField('备用字段',max_length=255,null=True,blank=True)
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

class permachine_info(models.Model):
    mac=models.CharField('MAC码',max_length=25,unique=True)
    macnum=models.CharField('数字码',max_length=25,null=True,blank=True)
    cpuid=models.CharField('CPUID',max_length=255,default="ffffffff-d4bd-1afb-3ba9-893c0033c587")
    spare=models.CharField('备用字段',max_length=255,null=True,blank=True)
    def __unicode__(self):
        return self.mac

class perauthorization(models.Model):
    mac=models.ForeignKey(permachine_info, related_name='app_pre_info')
    cpuid=models.CharField('CPUID',max_length=255,default="ffffffff-d4bd-1afb-3ba9-893c0033c587")
    appid=models.CharField('APPID',max_length=20,null=True,blank=True)
    ipaddress=models.GenericIPAddressField('访问的IP',null=True,blank=True)
    register_time=models.CharField('请求时间',max_length=255)
    perstate=models.CharField('处理状态',max_length=20,default=1)
    spare=models.CharField('备用字段',max_length=255,null=True,blank=True)

class accesslog(models.Model):
    mac=models.ForeignKey(authorization, related_name='access_log')
    cpuid=models.CharField('CPUID',max_length=255,default="ffffffff-d4bd-1afb-3ba9-893c0033c587")
    appid=models.CharField('APPID',max_length=20,null=True,blank=True)
    ipaddress=models.GenericIPAddressField('访问的IP',null=True,blank=True)
    aucode=models.CharField('授权码',max_length=255)
    a_time=models.CharField('鉴权时间',max_length=255,null=True,blank=True)
    dostate=models.CharField('鉴权状态',max_length=20)
    spare=models.CharField('备用字段',max_length=255,null=True,blank=True)
    def __unicode__(self):
        return self.aucode

class appinfo(models.Model):
    appid=models.CharField(max_length=50,unique=True)
    appname=models.CharField(max_length=255,null=True,blank=True)
    appdesc=models.CharField(max_length=255,null=True,blank=True)

class apprelate(models.Model):
    appid=models.ForeignKey(appinfo, related_name='app_info')
    version=models.CharField(max_length=255,unique=True)
    download_url=models.CharField(max_length=255,null=True,blank=True)