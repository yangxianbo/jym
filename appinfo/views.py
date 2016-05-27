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
from tools.handle_upfile import Handle_upfile
from tools.resolve_apk import readxml
#models
from appinfo.models import *

def quest_app(request):
    if request.POST:
        appid=request.POST['appid']
        try:
            app=appinfo.objects.get(appid=appid)
            data={'id':app.appid,'folder':app.appfolder,'version':app.version,'size':app.appsize,'url':app.downloadurl,'state':app.upstate,'logo':app.logourl}
            return HttpResponse(json.dumps(data), 'application/javascript')
        except Exception:
            raise Http404

@login_required()
def appinfo_index(request, template_name):
    if request.POST:
        localtime=UnixTime()
        appid=request.POST["appid"]
        appname=request.POST["appname"]
        appdesc=request.POST["appdesc"]
        upstate=request.POST['upstate']
        ticker=request.POST['ticker']
        if request.POST['action'] == 'add':
            try:
                new=appinfo.objects.create(
                                        appid=appid,
                                        appname=appname,
                                        appdesc=appdesc,
                                        upstate=upstate,
                                        ticker=ticker,
                                    )
                new.save()
                return HttpResponse('ok')
            except Exception as error:
                return HttpResponse(str(error))
        else:
            pid=request.POST['pk']
            appinfo.objects.filter(id=pid).update(appid=appid,appname=appname,appdesc=appdesc,upstate=upstate,ticker=ticker)
            return HttpResponse('ok')
    else:
        queryset=appinfo.objects.all().order_by('-pk')
        search_fields = ['appid','appfolder','appname']
        return get_datatables_records(
            request,
            queryset,
            search_fields,
            template_name,
            extra_context={
            })

@login_required()
def up_file(request):
    if request.POST:
        localtime=UnixTime()
        f=request.FILES['upfile']
        opera=request.POST['flag']
        pid=request.POST['pk']
        prefix=os.path.splitext(f.name)[-1]
        if prefix == ".apk" and opera == "upapp":
            upstate=Handle_upfile(f)
            if upstate != -1 and upstate != -2:
                apk_info=readxml(upstate)
                apkurl="http://appstoreapi.tvdfe.com:8090/%s"%os.path.basename(upstate)
                appinfo.objects.filter(id=pid).update(
                                            appfolder=apk_info[0],
                                            uptime=localtime,
                                            version=apk_info[1],
                                            appsize=apk_info[2],
                                            downloadurl=apkurl,
                                        )
                return HttpResponse('ok')
            else:
                return HttpResponse('无效操作')
        else:
            return HttpResponse('无效操作')

@login_required()
def show_app_data(request):
    import appinfo.models
    pk_tmp=request.POST['pk']
    tables=request.POST['table']
    db_models=getattr(appinfo.models, tables)
    data = serializers.serialize("json", db_models.objects.filter(**{'id':pk_tmp}))
    return HttpResponse(data, 'application/javascript')

@login_required()
def del_file(request):
    ''' 删除文件'''
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        apkdelete=appinfo.objects.filter(pk__in=tids).values_list('downloadurl')
        for apk in apkdelete:
            if apk[0] != None:
                os.system('rm -f ../upfile/%s'%os.path.basename(apk[0]))
        appinfo.objects.filter(pk__in=tids).delete()
    return HttpResponse('ok')

@login_required()
def force_apk(request):
    ''' 强制状态'''
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        appinfo.objects.filter(pk__in=tids).update(upstate=0)
    return HttpResponse('ok')

@login_required()
def normal_apk(request):
    ''' 强制状态'''
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        appinfo.objects.filter(pk__in=tids).update(upstate=1)
    return HttpResponse('ok')
