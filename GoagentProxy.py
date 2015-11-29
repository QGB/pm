s='''
"D:/Program Files/goagent_3.1.0-0/local/proxy.ini""
"E:/software/net/tool/XX-Net-1.3.6/goagent/3.1.40/local/proxy.ini"
"E:/software/net/tool/XX-Net-2.5.1/gae_proxy/local/proxy.ini"
"E:/software/net/tool/XX-Net-2.5.1/php_proxy/local/proxy.ini"

'''
from qgb import U,T,clipboard
import os,sys,re
sc=clipboard.get()
# sc=s

sc=sc.lower().replace('\\','/')

def isp(a):
	if(len(a)<11):return False
	if(a.find(":")!=1):return False
	if(a[-4-5:]!='proxy.ini'): return False
	return True

s127='''[listen]
ip = 127.0.0.1'''
s000='''[listen]
ip = 0.0.0.0'''
def rep(a):
	f=open(a)
	s=f.read()
	f.close()
	s=s.replace(s127,s000)
	
	f=open(a,'w')
	f.write(s)
	f.close()
	print s[:44]
sq=r'"'

if(len(sc)<11 or sc==None or sc.find('proxy.ini')==-1):
	sc=s
# print sc

ls=[]
sc0=T.sub(sc,sq,sq)
if(len(sc0)>5):
	for i in sc.split(sq):
		print U.ct()
		if(isp(i)):
			print i,'\n','='*33
			rep(i)