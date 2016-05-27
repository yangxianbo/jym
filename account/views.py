#coding:utf-8
# Create your views here.
import os, sys, commands, re, time, json
from django.shortcuts import render_to_response, get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader, Context
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import HttpResponse
from tools.utils import get_datatables_records
from django.contrib import admin
from account.models import UserProfile, UserGroup
from django.core import serializers
from account.decorator import login_required

@login_required()
def user_index(request, template_name):
    ''' 用户中心 '''
    queryset = UserProfile.objects.all()
    search_fields = ['user__username', 'id']
    if request.POST:
        first_name=request.POST["first_name"]
        username=request.POST["username"]
        password=request.POST["password"]
        mobile=request.POST["mobile"]
        is_active=request.POST["is_active"]

        if request.POST['is_create'] == "true":
            is_create = 0
        else:is_create = 1
        if request.POST['is_modify'] == "true":
            is_modify = 0
        else:is_modify = 1
        if request.POST['is_delete'] == "true":
            is_delete = 0
        else:is_delete = 1
        email=request.POST["email"]
        department=request.POST["department"]

        if request.POST['action'] == 'add':
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name=first_name
                if is_active == "true":
                    user.is_staff=True
                else:
                    user.is_staff=False
                user.save()
                UserProfile.objects.filter(user__username=username).update(mobile=mobile, department=department,is_delete=is_delete,is_create=is_create,is_modify=is_modify)
                return HttpResponse('ok')
            except Exception as error:
                return HttpResponse(str(error))
        else:
            pk=request.POST["pk"]
            try:
#                user = User.objects.filter(username=username).update(username=username, email=email,first_name=first_name)
                if is_active == "true":
                    User.objects.filter(id=pk).update(username=username, email=email,first_name=first_name, is_active=1)
                else:
                    User.objects.filter(id=pk).update(username=username, email=email,first_name=first_name,is_active=0)
                UserProfile.objects.filter(user__username=username).update(mobile=mobile, department=department,is_delete=is_delete,is_create=is_create,is_modify=is_modify)
                return HttpResponse('ok')
            except Exception as error:
                return HttpResponse(str(error))

    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
            'queryset_user': queryset
        })

@login_required()
def show_md_data(request):
    import account.models
    pk_tmp=request.POST['pk']
    tables=request.POST['tables']
    db_models=getattr(account.models, tables)
    data = serializers.serialize("json", db_models.objects.filter(**{'id':pk_tmp}))

    if tables == 'UserProfile':
        d=json.loads(data)
        u=User.objects.get(id=d[0]['fields']['user'])
        d[0]['fields']['username']=u.username
        d[0]['fields']['first_name']=u.first_name
        d[0]['fields']['email']=u.email
        d[0]['fields']['is_active']=u.is_active
        return  HttpResponse (json.dumps(d), 'application/javascript')
    return HttpResponse(data, 'application/javascript')

@login_required()
def del_user_index(request):
    ''' 删除用户'''
    pk = request.REQUEST.get('pk')
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        User.objects.filter(id__in=tids).delete()
    return HttpResponse('ok')


@login_required()
def group_index(request, template_name):
    ''' 组管理 '''
    if request.POST:
        gname=request.REQUEST.get("gname")
        members=request.REQUEST.getlist("members")
        members_id_all=[]
        for row_id in members:
            members_id_all.append(str(row_id))

        if request.POST['action'] == 'add':
            try:
                UserGroup.objects.create(
                    gname=gname,
                    members=",".join(members_id_all)
                )
                return HttpResponse('ok')
            except Exception as error:
                return HttpResponse(str(error))
        else:
            pk=request.POST['pk']
            try:
                UserGroup.objects.filter(pk=pk).update(
                    gname=gname,
                    members=",".join(members_id_all)
                )
                return HttpResponse('ok')
            except Exception as error:
                return HttpResponse(str(error))

    queryset=UserGroup.objects.all()
    user_list=UserProfile.objects.all()
    search_fields = ['gname']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
            'user_list':user_list
        })


@login_required()
def delete_count(request):
    import account.models
    pk = request.POST['pk']
    tables=request.POST['tables']
    print tables
    db_models=getattr(account.models, tables)
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        db_models.objects.filter(id__in=tids).delete()
    return HttpResponse('ok')
