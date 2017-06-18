# -*- coding: utf-8 -*-
from qgb import U,T
from urllib2 import *
import chardet
import sys,os
import re


d=[];
sfr='cdefg'
# def geth(fn):
	# global d
	
def find(ap):
	d=[]
	try:
		fs=os.listdir(ap)
	except Exception as err:
		print str(err)
		return []
	for fn in fs:
		f=ap+fn
		#print '------'+f
		if(os.path.isfile(f)):
			d.append(fn)
			# ict=U.ct()
			# ind=29998
			# # if ind<ict<ind+30:print f
			# if ict>ind+999:return d
			
			# d[hash()]
		else:
			f=f+'/'
			#print f
			d.append(find(f))
	return d

d=find('c:/')
U.phtml('ctest')
U.pprint(d)
U.phtmlend()
type(d)


# for root in sfr:
# 	root+=':/'
# 	# print root
# 	find(root)
exit()




exit()
reload(sys)
sys.setdefaultencoding("utf-8")
url='''http://218.196.43.18:8888/fckeditor/editor/filemanager/connectors/aspx/connector.aspx?Command=GetFoldersAndFiles&Type=File&CurrentFolder=d:/'''

import mp3play


exit()

sxml= urlopen(url).read()
# U.write('fck.xml',sxml)
sxml=U.read('fck.xml')
# sxml=sxml.decode('utf-8')
print chardet.detect(sxml)

s=U.read('fck.xml')
s=s.decode('utf-8')
print s[2899:2911]
exit()
import os
# os.system('ls|grep u')

import chardet

sc='ccsu文档资料'
print type(sc)

print chardet.detect(sc)

#

sc= sc.decode('utf-8')
print type(sc)