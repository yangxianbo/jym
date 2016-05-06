#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-04-02 15:26:36
#FILENAME: a.py
#DESCRIPTION: 
#===============================================================


from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

#def md5key(key):
#    import hashlib
#    m=hashlib.md5(key)
#    m.digest()
#    md5=m.hexdigest() 
#    return md5
#print md5key("Eesyvideo20160402_yw")

class Aucode():
    def __init__(self,words,func):
        self.words=words
        self.func=func
        key="a8e39d5a209af8ee2a4cb285dd9d500e"
        self.cryptor=AES.new(key)

    def _encrypt(self):
        BS=AES.block_size
        pad=lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        entext=b2a_hex(self.cryptor.encrypt(pad(self.words)))
        return entext

    def _decrypt(self):
        unpad=lambda s : s[0:-ord(s[-1])]
        try:
            detext=unpad(self.cryptor.decrypt(a2b_hex(self.words)))
            if detext == "":
                return -3
            else:
                info_list=detext.split("+")
                if len(info_list) == 3:
                    return info_list
                else:
                    return -4
        except Exception,e:
            return -2

    def main(self):
        if self.func == 0:
            return self._encrypt()
        elif self.func == 1:
            return self._decrypt()
        else:
            return -1
