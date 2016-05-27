# Create your views here.
# -*- coding: utf-8 -*-
import os, sys, commands, re, time
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader, Context
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import HttpResponse
from account.decorator import login_required

def Login(request, template_name):
    ''' 登录 '''
    vt = loader.get_template(template_name)
    if request.POST:
        print request.POST
        loguser = request.POST['username']
        logpass = request.POST['password']
        user = authenticate(username=loguser, password=logpass)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/app/appindex/")
        return HttpResponseRedirect("/user/login/")
    c = RequestContext(request,{})
    return HttpResponse(vt.render(c))

@login_required()
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/user/login/')

@login_required()
def change_password(request):
    if request.method == 'POST':
        oldps  = request.POST['oldps']
        newps1 = request.POST['newps1']
        newps2 = request.POST['newps2']

        if not oldps or not newps1 or not newps2:
            return HttpResponse('任意一项都不能为空!')

        if newps1 != newps2:
            return HttpResponse('2次密码不一致!')

        user = authenticate(username=request.user.username, password=oldps)
        if not user:
            return HttpResponse('旧密码错误!')
        else:
            Modify = User.objects.get(username=request.user.username)
            Modify.set_password(newps1)
            Modify.save()
            return HttpResponse("ok")

    return HttpResponse("错误,你是who?")
