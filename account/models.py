#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    department = models.CharField('部门', max_length=255, default="未知")
    mobile = models.CharField('联系电话', max_length=255, default="未知")
    access_list = models.CharField('权限列表', max_length=255, default="未知", null=True)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)


class UserGroup(models.Model):
    gname = models.CharField('名字', max_length=255)
    members  = models.CharField('成员', max_length=255)

class mail_server(models.Model):
    """ 报警消息 """
    mailserver = models.CharField('服务器地址', max_length=255)
    mailuser = models.CharField('用户名', max_length=255)
    mailpasswd = models.CharField('密码', max_length=255)
