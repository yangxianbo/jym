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
from tools.handle_upfile import Handle_upfile
from tools.recoder_auth import Recoder_auth
from tools.aucode import Aucode
#models
from authsys.models import *


def manage_auth(request):
    ip=getip(request)
    localtime=UnixTime()
    if request.method == 'POST':
        jstring=request.body
        manage=json.loads(jstring)
        if isinstance(manage,dict):
            try:
                mac=manage['mac']
                cpuid=manage['cpuid']
                appid=manage['appid']
                find_list=authorization.objects.filter(Q(mac__mac=mac)&Q(appid=appid))
                if len(find_list) != 0:
                    auinfo=find_list[0]
                    if int(auinfo.austate) != 1:
                        manage['aucode']=auinfo.aucode            
                        return HttpResponse(json.dumps(manage ,indent=4,ensure_ascii=False), 'application/javascript')
                    else:
                        return HttpResponse(-9001)
                else:
                    try:
                        fkey=permachine_info.objects.get(mac=mac)
                        find_per_list=perauthorization.objects.filter(Q(mac__mac=mac)&Q(appid=appid))
                        if len(find_per_list) != 0:
                            update_perauth=find_per_list[0]
                            update_perauth.register_time=localtime
                            update_perauth.ipaddress=ip
                            update_perauth.save()
                            return HttpResponse(1)
                        else:
                            create_perauth=perauthorization.objects.create(mac=fkey,appid=appid,cpuid=cpuid,register_time=localtime,ipaddress=ip)
                            create_perauth.save()
                            return HttpResponse(2)
                    except permachine_info.DoesNotExist:
                        macnum=int(mac,16)
                        create_permachine=permachine_info.objects.create(mac=mac,cpuid=cpuid,macnum=macnum)
                        create_permachine.save()
                        pkey=permachine_info.objects.get(mac=mac)
                        create_perauth=perauthorization.objects.create(mac=pkey,appid=appid,cpuid=cpuid,register_time=localtime,ipaddress=ip)
                        create_perauth.save()
                        return HttpResponse(2)
            except KeyError:
                return HttpResponse(-9002)
        else:
            raise Http404

def check_auth(request):
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
                check_status=Checkauth(mac,cpuid,appid,aucode,ip,localtime)
                return HttpResponse(check_status)
            except KeyError:
                return HttpResponse(-9002)
        else:
            raise Http404

@login_required()
def check_file(request, template_name):
    _status = request.REQUEST.get('status', "0")
    if str(_status) == "1":
        queryset=upload_file.objects.filter(status="1").order_by("-id")
    else:
        queryset=upload_file.objects.filter(status="0").order_by("-id")
    search_fields = ['filename', 'filepath','status']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
            'status':_status
        })

@login_required()
def up_file(request):
    if request.method == 'POST':
        dostate=request.POST['_isactive']
        f=request.FILES['upfile']
        upstate=Handle_upfile(f)
        if upstate != -1 and upstate != -2:
            localtime=UnixTime()
            if dostate == "":
                check_file=upload_file.objects.filter(filename=f.name)
                if len(check_file) == 0:
                    upload_file.objects.create(filename=f.name,filepath=upstate,createtime=localtime)
                else:
                    check_file.update(createtime=localtime,status=1)
                return HttpResponse("up_ok")
            elif dostate == "on":
                check_file=upload_file.objects.filter(filename=f.name)
                if len(check_file) == 0:
                    dofile=Recoder_auth(upstate)
                    dofile.main()
                    upload_file.objects.create(filename=f.name,filepath=upstate,status=0,createtime=localtime,dotime=localtime)
                else:
                    dofile=Recoder_auth(upstate)
                    dofile.main()
                    check_file.update(createtime=localtime,status=0,dotime=localtime)
                return HttpResponse("do_ok")
            else:
                return HttpResponse(-9003)
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
        upload_file.objects.filter(id__in=tids).delete()
    return HttpResponse('ok')

@login_required()
def do_file(request):
    ''' 执行文件'''
    localtime=UnixTime()
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        filedo=upload_file.objects.filter(id__in=tids).values_list('filepath')
        for filename in filedo:
            dofile=Recoder_auth(filename[0])
            dofile.main()
        upload_file.objects.filter(id__in=tids).update(status=0,dotime=localtime)
    return HttpResponse('ok')

@login_required()
def authgroup_index(request, template_name):
    queryset=group_info.objects.all()
    search_fields = [ 'agency']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
        })


@login_required()
def add_group(request):
    try:
        agency=request.POST['agency']
        groupdesc=request.POST['desc']
        add=group_info.objects.create(agency=agency,groupdesc=groupdesc)
        add.save()
        return HttpResponse('ok')
    except Exception,e:
        return HttpResponse(e)

@login_required()
def del_group(request):
    ''' 删除组'''
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        gkey=group_info.objects.filter(id__in=tids)
        grouplist=[]
        for agency in gkey.values_list('agency'):
            grouplist.append(agency[0])
        machine_info.objects.filter(agency__in=grouplist).delete
        gkey.delete()
    return HttpResponse('ok')

@login_required()
def update_group(request):
    ''' 更新组'''
    pk=request.POST['upid']
    agency=request.POST['agency']
    groupdesc=request.POST['desc']
    gkey=group_info.objects.filter(pk=pk)
    basename=gkey.values_list('agency')[0][0]
    gkey.update(agency=agency,groupdesc=groupdesc)
    machine_info.objects.filter(agency=basename).update(agency=agency)
    return HttpResponse('ok')

@login_required()
def package_index(request, template_name):
    queryset=package.objects.all()
    search_fields = ['packageid','packagename']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
        })

@login_required()
def add_package(request):
    try:
        packageid=request.POST['packageid']
        packagename=request.POST['packagename']
        autime=request.POST['autime']
        if len(package.objects.filter(packageid=packageid)) == 0:
            add=package.objects.create(packageid=packageid,packagename=packagename,autime=autime)
            add.save()
            return HttpResponse('ok')
        else:
            return HttpResponse('已存在相同APPID')
    except Exception,e:
        return HttpResponse(e)

@login_required()
def update_package(request):
    pk=request.POST['pid']
    packagename=request.POST['packagename']
    autime=request.POST['autime']
    package.objects.filter(pk=pk).update(packagename=packagename,autime=autime)
    return HttpResponse('ok')

@login_required()
def del_package(request):
    ''' 删除关联'''
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        package.objects.filter(id__in=tids).delete()
    return HttpResponse('ok')

@login_required()
def relate_index(request, template_name):
    _pid = request.REQUEST.get('pk', "0")
    if _pid != "0":
        pkey=package.objects.get(pk=_pid)
        queryset=package_relateapp.objects.filter(packageid=pkey)
    search_fields = ['appid']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
            'packagename':pkey.packagename,
            'pid':_pid,
        })

@login_required()
def add_relate(request):
    try:
        pid=request.POST['pid']
        appid=request.POST['appid']
        playid=request.POST['playid']
        if len(package_relateapp.objects.filter(packageid_id=pid,appid=appid)) == 0:
            add=package_relateapp.objects.create(packageid_id=pid,appid=appid,playid=playid)
            add.save()
            return HttpResponse('ok')
        else:
            return HttpResponse('已存在相同APPID')
    except Exception,e:
        return HttpResponse(e)

@login_required()
def update_relate(request):
    ''' 更新关联'''
    pid=request.POST['pid']
    playid=request.POST['playid']
    appid=request.POST['appid']
    package_relateapp.objects.filter(packageid_id=pid,appid=appid).update(playid=playid)
    return HttpResponse('ok')

@login_required()
def del_relate(request):
    ''' 删除关联'''
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        package_relateapp.objects.filter(id__in=tids).delete()
    return HttpResponse('ok')

@login_required()
def machine_index(request, template_name):
    queryset_group=group_info.objects.all()
    queryset=machine_info.objects.all().order_by('-pk')
    search_fields = ['mac','macnum','cpuid','agency']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
            'gname':queryset_group,
        })

@login_required()
def add_machine(request):
    try:
        mac=request.POST['mac']
        cpuid=request.POST['cpuid']
        agency=request.POST['agency']
        macnum=int(mac,16)
        if cpuid != "":
            new=machine_info.objects.create(mac=mac,cpuid=cpuid,macnum=macnum,agency=agency)
        else:
            new=machine_info.objects.create(mac=mac,macnum=macnum,agency=agency)
        new.save()
        return HttpResponse('ok')
    except Exception,e:
        return HttpResponse(e)

@login_required()
def update_machine(request):
    try:
        pk=request.POST['pk']
        mac=request.POST['mac']
        macnum=int(mac,16)
        cpuid=request.POST['cpuid']
        agency=request.POST['agency']
        if cpuid != "" :
            machine_info.objects.filter(pk=pk).update(mac=mac,agency=agency,cpuid=cpuid,macnum=macnum)
        else:
            machine_info.objects.filter(pk=pk).update(mac=mac,agency=agency,macnum=macnum)
        return HttpResponse('ok')
    except Exception,e:
        return HttpResponse(e)

@login_required()
def del_machine(request):
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
       machine_info.objects.filter(id__in=tids).delete()
    return HttpResponse('ok')

@login_required()
def auth_info(request, template_name):
    if request.POST:
        try:
            pid=request.POST['pid']
            mac=request.POST['mac']
            cpuid=request.POST['cpuid']
            appid=request.POST['appid']
            playid=request.POST['playid']
            s_time=request.POST['s_time']
            autime=request.POST['autime']
            austate=request.POST['austate']
            getcode=Aucode("%s+%s+%s"%(mac,cpuid,appid),0)
            aucode=getcode.main()
            if request.POST['action'] == 'add':
                if len(authorization.objects.filter(mac_id=pid,appid=appid)) == 0:
                    e_time=stime_change_time(time_change_stime(s_time)+(int(autime)*86400))
                    new=authorization.objects.create(mac_id=pid,appid=appid,playid=playid,s_time=s_time,e_time=e_time,autime=autime,aucode=aucode)
                    new.save()
                    return HttpResponse('ok')
                else:return HttpResponse('APPID已存在')
            else:
                pk=request.POST['pk']
                if len(authorization.objects.filter(mac_id=pid,appid=appid)) == 0:
                    e_time=stime_change_time(time_change_stime(s_time)+(int(autime)*86400))
                    authorization.objects.filter(pk=pk).update(appid=appid,playid=playid,s_time=s_time,e_time=e_time,autime=autime,aucode=aucode)
                    return HttpResponse('ok')
                else:return HttpResponse('APPID已存在')
        except Exception,e:
            return HttpResponse(e)
    else:
        _pid = request.REQUEST.get('pk', "0")
        if _pid != "0":
            mkey=machine_info.objects.get(pk=_pid)
            queryset=authorization.objects.filter(mac=mkey).order_by('appid')
            mac=mkey.mac
            cpuid=mkey.cpuid
            agency=mkey.agency
        search_fields = ['appid','playid','austate']
        return get_datatables_records(
            request,
            queryset,
            search_fields,
            template_name,
            extra_context={
                'mac':mac,
                'cpuid':cpuid,
                'pid':_pid,
                'agency':agency,
            })

@login_required()
def del_auth(request):
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        authorization.objects.filter(id__in=tids).delete()
    return HttpResponse('ok')

@login_required()
def show_au_data(request):
    import authsys.models
    pk_tmp=request.POST['pk']
    tables=request.POST['table']
    db_models=getattr(authsys.models, tables)
    data = serializers.serialize("json", db_models.objects.filter(**{'id':pk_tmp}))
    return HttpResponse(data, 'application/javascript')

@login_required()
def access_log(request, template_name):
    _pid = request.REQUEST.get('pk', "0")
    if _pid != "0":
        mac=request.GET['mac']
        appid=request.GET['appid']
        stime = request.GET['start_time']
        etime = request.GET['end_time']
        _t = request.REQUEST.get('t', "today")
        queryset=accesslog.objects.filter(mac_id=_pid,appid=appid,a_time__range=[stime,etime])

    search_fields = ['appid','dostate']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
            't':_t,
            'u_stime':stime,
            'u_etime':etime,
            'mac':mac,
            'pid':_pid,
            'appid':appid,
        })

@login_required()
def pre_machine(request, template_name):
    queryset=premachine_info.objects.all()
    search_fields = ['mac','macnum']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
        })
    
@login_required()
def del_premachine(request):
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        premachine_info.objects.filter(id__in=tids).delete()
    return HttpResponse('ok')

@login_required()
def pre_authinfo(request, template_name):
    _pid = request.REQUEST.get('pk', "0")
    if _pid != "0":
        pkey=premachine_info.objects.get(id=_pid)
        mac=pkey.mac
        queryset=preauthorization.objects.filter(mac_id=_pid)
    search_fields = ['appid']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
            'mac':mac,
            'pid':_pid,
        })

@login_required()
def do_auth(request):
    if request.POST:
        mac=request.POST['mac']
        cpuid=request.POST['cpuid']
        pid=request.POST['pid']
        appid=request.POST['appid']
        playid=request.POST['playid']
        autime=request.POST['autime']
        getcode=Aucode("%s+%s+%s"%(mac,cpuid,appid),0)
        aucode=getcode.main()
        
