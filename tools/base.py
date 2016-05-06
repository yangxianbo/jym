#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-04-13 01:08:56
#FILENAME: base.py
#DESCRIPTION: 
#===============================================================


import sys,os
append_path=os.path.abspath('../')
sys.path.append(append_path)
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ECM.settings")
application = get_wsgi_application()
