# -*- coding: utf-8 -*-
# Create your views here.
import time
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext,loader
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

def UnixTime(day=0, FORMAT="%Y-%m-%d %H:%M:%S"):
    return time.strftime(FORMAT, time.localtime(time.time()-86400*day))

def timestamp(day=0):
    t = UnixTime(day)
    return int(time.mktime(time.strptime(t,'%Y-%m-%d %H:%M:%S')))

def stime_change_time(t):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(float(t)))

def time_change_stime(t):
    return int(time.mktime(time.strptime(t,'%Y-%m-%d %H:%M:%S')))

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
         try:
             return dict.__getitem__(self, item)
         except KeyError:
             value = self[item] = type(self)()
             return value


def keyWorld_Search(queryset, request, search_fields):
    ''' 根据search_fields来查询 '''
    SearchKey = request.REQUEST.get('search')
    outputQ = None
    kwargs = {}
    for t_field in search_fields:
        keywords = request.REQUEST.get(t_field)
        if keywords:
            kwargs[t_field] = keywords
        if SearchKey:
            kwargz = {t_field + "__icontains": SearchKey}
            outputQ = outputQ | Q(**kwargz) if outputQ else Q(**kwargz)

    if len(kwargs) >= 1:
        return queryset.filter( **kwargs )
    elif outputQ:   
        return queryset.filter(outputQ).distinct()
    else:
        return queryset

def get_datatables_records(request, queryset, search_fields, template_name, extra_context={}):
    '''
     该函数实现了分页功能!
     queryset 一个Sql对象
     template_name 模板文件
     extra_context 包含参数等信息
    '''

    status = request.GET.get('status', '0')

    # 分组功能
    member=request.GET.get("member", 'null')
    if member != 'null' and member:
        _ids=[]
        for ids in member.split(','):
            _ids.append(int(ids))
        queryset=queryset.filter(id__in=_ids)

    gname=request.GET.get("gname", 'null')
    after_range_num = 5
    bevor_range_num = 4

    if status == '1' or status == '2':
        queryset_status=queryset.filter(status__in=['1','2'])
    else:
        queryset_status=queryset

    input_order=request.GET.get("inputOrder", 'null')
    _input_order='null'
    if input_order != 'null':
        _order=input_order.split('|')
        if _order[1] == "desc":
            queryset_desc=queryset_status.order_by(_order[0])
        elif _order[1] == "asc":
            queryset_desc=queryset_status.order_by('-%s' % _order[0])
        else:
            queryset_desc=queryset_status
        _input_order=_order[1]
    else:
        queryset_desc=queryset_status

    print _input_order
    _queryset = keyWorld_Search(queryset_desc, request, search_fields)

    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1

    pagesize = request.GET.get('pagesize', 20)
    paginator = Paginator(_queryset, int(pagesize))

    try:
        object_result = paginator.page(page)
    except:
    #except(EmptyPage,InvalidPage,PageNotAnInteger):
        object_result = paginator.page(1)

    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+bevor_range_num]

    context = {
        'object_result':object_result,
        'request':request,
        'gname':gname,
        'queryset':_queryset,
        'page_range':page_range,
        'pagesize':pagesize,
        'page':page,
        'input_orders':_input_order,
        'status':status
    }
    ''' 附加extra_context到context '''
    context.update(extra_context)
    vt = loader.get_template(template_name)
    return HttpResponse(vt.render(RequestContext(request,context)))

def getip(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip=request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip=request.META['REMOTE_ADDR']
    return ip

