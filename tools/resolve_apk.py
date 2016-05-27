#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-04-27 16:39:27
#FILENAME: resolve_apk.py
#DESCRIPTION: 
#===============================================================


from __future__ import division
import os
import axmlparserpy.axmlprinter as axmlprinter
from xml.dom import minidom
from xml.dom.minidom import parseString

def readxml(filename):
    size=float('%0.1f'%(os.path.getsize(filename)/1024/1024))
    os.system('unzip -f %s "AndroidManifest.xml" -d /tmp/'%filename)
    ap = axmlprinter.AXMLPrinter(open('/tmp/AndroidManifest.xml', 'rb').read())
    buff = minidom.parseString(ap.getBuff()).toxml()
    getxml=parseString(buff)
    version=getxml.getElementsByTagName("manifest")[0].getAttribute('android:versionCode')
    floder=getxml.getElementsByTagName("manifest")[0].getAttribute('package')
    return [floder,version,"%sM"%size]
