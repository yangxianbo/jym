#coding:utf-8
#通用类
import os, sys, commands, re, time, json
from django.shortcuts import render_to_response, get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core import serializers
from django.template import RequestContext, loader, Context
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import HttpResponse
from django.contrib import admin
from account.decorator import login_required
from django.http import Http404
from django.db.models import Q
#tools
from tools.utils import get_datatables_records,UnixTime,time_change_stime,timestamp,stime_change_time,getip
from tools.checkauth import Checkauth
from tools.getlist import Getlist
#models
from playlist.models import upload_file,playgroup,liveplaylist


def get_playlist(request):
    ip=getip(request)
    localtime=UnixTime()
    if request.method == 'POST':
        jstring=request.body
        check=json.loads(jstring)
        if isinstance(check,dict):
            try:
                mac=check['mac']
                cpuid=check['cpuid']
                appid=check['appid']
                aucode=check['aucode']
                playlist=Getlist(mac,cpuid,appid,aucode,ip,localtime)
                return HttpResponse(json.dumps(playlist ,indent=4,ensure_ascii=False), 'application/javascript')
            except KeyError:
                return HttpResponse(-9002)
        else:
            raise Http404
