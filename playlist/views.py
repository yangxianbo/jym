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
from tools.handle_upfile import Handle_upfile
from tools.recoder_list import Recoder_list
#models
from playlist.models import * 


def get_playlist(request):
    ip=getip(request)
    localtime=UnixTime()
    if request.method == 'POST':
        mac=request.POST['mac']
        cpuid=request.POST['cpuid']
        appid=request.POST['appid']
        aucode=request.POST['aucode']
        playlist=Getlist(mac,cpuid,appid,aucode,ip,localtime)
        return HttpResponse(json.dumps(playlist ,indent=4,ensure_ascii=False), 'application/javascript')
    else:
        raise Http404

@login_required()
def up_logo(request):
    if request.POST:
        f=request.FILES['upfile']
        opera=request.POST['flag']
        pid=request.POST['pk']
        cid=request.POST['channelid']
        prefix=os.path.splitext(f.name)[-1]
        if (prefix == ".jpg" or prefix == ".gif" or prefix == ".png") and opera == "uplogo":
            upstate=Handle_upfile(f)
            if upstate != -1 and upstate != -2:
                logourl="http://appstoreapi.tvdfe.com:8090/%s"%os.path.basename(upstate)
                liveplaygroup_adv.objects.filter(livegroupid_id=pid,channelid=cid).update(advurl=logourl)
                return HttpResponse('ok')
            else:
                return HttpResponse('无效操作')
        else:
            return HttpResponse('无效操作')

@login_required()
def livegroup_index(request, template_name):
    queryset=liveplaygroup.objects.all()
    search_fields = ['livegroupid']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
        })

@login_required()
def add_livegroup(request):
    try:
        livegroupid=request.POST['livegroupid']
        livegroupname=request.POST['livegroupname']
        livegroupdesc=request.POST['livegroupdesc']
        liverelate_id=request.POST['liverelate_id']
        if len(liveplaygroup.objects.filter(livegroupid=livegroupid)) == 0:
            add=liveplaygroup.objects.create(livegroupid=livegroupid,livegroupname=livegroupname,livegroupdesc=livegroupdesc,liverelate_id=liverelate_id)
            add.save()
            return HttpResponse('ok')
        else:
            return HttpResponse('已存在相同APPID')
    except Exception,e:
        return HttpResponse(e)

@login_required()
def update_livegroup(request):
    pk=request.POST['pid']
    livegroupid=request.POST['livegroupid']
    livegroupname=request.POST['livegroupname']
    livegroupdesc=request.POST['livegroupdesc']
    liverelate_id=request.POST['liverelate_id']
    cid_list=liverelate_id.split(',')
    liveplaygroup.objects.filter(pk=pk,livegroupid=livegroupid).update(livegroupname=livegroupname,livegroupdesc=livegroupdesc,liverelate_id=liverelate_id)
    for cid in cid_list:
        if len(liveplaygroup_adv.objects.filter(livegroupid_id=pk,channelid=cid)) == 0:
            newadv=liveplaygroup_adv.objects.create(livegroupid_id=pk,channelid=cid)
            newadv.save()
        else:
            pass
    origin_list=liveplaygroup_adv.objects.filter(livegroupid_id=pk).values_list('channelid')
    ocid_list=[]
    for ocid in origin_list:
        ocid_list.append(ocid[0])
    diff_list=list(set(ocid_list).difference(set(cid_list)))
    liveplaygroup_adv.objects.filter(livegroupid_id=pk,channelid__in=diff_list).delete()
    return HttpResponse('ok')

@login_required()
def del_livegroup(request):
    ''' 删除关联'''
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        liveplaygroup.objects.filter(id__in=tids).delete()
    return HttpResponse('ok')

@login_required()
def live_index(request, template_name):
    if request.POST:
        try:
            channelid=request.POST['channelid']
            playname=request.POST['playname']
            classname=request.POST['classname']
            playaddress=request.POST['playaddress']
            mstatus=request.POST['mstatus']
            picurl=request.POST['picurl']
            if request.POST['action'] == 'add':
                if len(liveplaylist.objects.filter(playaddress=playaddress,playname=playname)) == 0:
                    new=liveplaylist.objects.create(channelid=channelid,playname=playname,classname=classname,playaddress=playaddress,mstatus=mstatus,picurl=picurl)
                    new.save()
                    return HttpResponse('ok')
                else:return HttpResponse('播放地址已存在')
            else:
                pk=request.POST['pk']
                liveplaylist.objects.filter(pk=pk).update(channelid=channelid,playname=playname,classname=classname,playaddress=playaddress,mstatus=mstatus,picurl=picurl)
                return HttpResponse('ok')
        except Exception,e:
            return HttpResponse(e)
    else:
        queryset=liveplaylist.objects.all()
        livegroup=liveplaygroup.objects.all()
        search_fields = ['channelid','playname','classname','playaddress']
        return get_datatables_records(
            request,
            queryset,
            search_fields,
            template_name,
            extra_context={
                'group':queryset,
                'livegroup':livegroup,
            })

@login_required()
def up_mpic(request):
    if request.POST:
        f=request.FILES['upfile']
        opera=request.POST['flag']
        pid=request.POST['pk']
        prefix=os.path.splitext(f.name)[-1]
        if prefix == ".jpg" or prefix == ".png" or prefix == ".gif"and opera == "upic":
            upstate=Handle_upfile(f)
            if upstate != -1 and upstate != -2:
                picurl="http://appstoreapi.tvdfe.com:8090/%s"%os.path.basename(upstate)
            liveplaylist.objects.filter(id=pid).update(picurl=picurl)
            return HttpResponse('ok')
        else:
            return HttpResponse('无效操作')


@login_required()
def show_live_data(request):
    import playlist.models
    pk_tmp=request.POST['pk']
    tables=request.POST['table']
    db_models=getattr(playlist.models, tables)
    data = serializers.serialize("json", db_models.objects.filter(**{'id':pk_tmp}))
    return HttpResponse(data, 'application/javascript')

@login_required()
def del_live(request):
    ''' 删除文件'''
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        liveplaylist.objects.filter(pk__in=tids).delete()
    return HttpResponse('ok')

@login_required()
def force_live(request):
    ''' 维护状态'''
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        liveplaylist.objects.filter(pk__in=tids).update(mstatus=0)
    return HttpResponse('ok')

@login_required()
def normal_live(request):
    ''' 正常状态'''
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        liveplaylist.objects.filter(pk__in=tids).update(mstatus=1)
    return HttpResponse('ok')
                                 
@login_required()
def relate_live(request):
    ''' 关联直播组'''
    gpk=request.POST['livegroupid']
    pk=request.POST['pk'].strip(',')
    relate_list=liveplaygroup.objects.filter(pk=gpk).values_list('liverelate_id')[0][0]
    cid_list=pk.split(',')
    union_list=list(set(cid_list).union(set(relate_list)))
    if len(list(set(cid_list).difference(set(relate_list)))) != 0:
        union_str=','.join(union_list).strip(',')
        liveplaygroup.objects.filter(pk=gpk).update(liverelate_id=union_str)
        for cid in cid_list:
            if len(liveplaygroup_adv.objects.filter(livegroupid_id=gpk,channelid=cid)) == 0:
                newadv=liveplaygroup_adv.objects.create(livegroupid_id=gpk,channelid=cid)
                newadv.save()
            else:
                pass
        origin_list=liveplaygroup_adv.objects.filter(livegroupid_id=gpk).values_list('channelid')
        ocid_list=[]
        for ocid in origin_list:
            ocid_list.append(ocid[0])
        diff_list=list(set(ocid_list).difference(set(union_list)))
        liveplaygroup_adv.objects.filter(livegroupid_id=gpk,channelid__in=diff_list).delete()
        return HttpResponse('ok')
    else:
        return HttpResponse('ok')

@login_required()
def file_index(request, template_name):
    queryset=upload_file.objects.all()
    search_fields = ['filename','filepath']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
        })

@login_required()
def up_file(request):
    if request.method == 'POST':
        f=request.FILES['upfile']
        upstate=Handle_upfile(f)
        if upstate != -1 and upstate != -2:
            localtime=UnixTime()
            new=upload_file.objects.create(filename=f.name,filepath=upstate,createtime=localtime)
            new.save()
            addlist=Recoder_list(upstate)
            addlist.main()
            return HttpResponse("ok")
        elif upstate == -2:
            return HttpResponse("uptype_wrong")
    else:
        return HttpResponse(-9003)

@login_required()
def del_file(request):
    ''' 删除文件'''
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        filedelete=upload_file.objects.filter(id__in=tids).values_list('filepath')
        for filename in filedelete:
            os.system('rm -f %s'%filename[0])
        upload_file.objects.filter(pk__in=tids).delete()
    return HttpResponse('ok')

@login_required()
def live_adv(request, template_name):
    _pid = request.REQUEST.get('pk', "0")
    if _pid != "0":
        pkey=liveplaygroup.objects.get(pk=_pid)
        channel_list=pkey.liverelate_id.split(',')
        c_dict={}
        for channelid in channel_list:
            pname=liveplaylist.objects.get(id=channelid).playname
            c_dict[channelid]=pname
        queryset=liveplaygroup_adv.objects.filter(livegroupid=pkey)
    search_fields = []
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
            'livegroupname':pkey.livegroupname,
            'pid':_pid,
            'relate':json.dumps(c_dict),
        })

@login_required()
def update_liveadv(request):
    if request.POST:
        advurl=request.POST['advurl']
        pid=request.POST['pid']
        cid=request.POST['cid']
        liveplaygroup_adv.objects.filter(livegroupid_id=pid,channelid=cid).update(advurl=advurl)
        return HttpResponse('ok')

@login_required()
def up_adv(request):
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    print tids
    if len(tids) > 0:
        liveplaygroup_adv.objects.filter(id__in=tids).update(advstate=0)
    return HttpResponse('ok')

@login_required()
def dis_adv(request):
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        liveplaygroup_adv.objects.filter(id__in=tids).update(advstate=1)
    return HttpResponse('ok')
