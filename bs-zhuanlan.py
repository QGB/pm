# -*- coding: cp936 -*-
from bs4 import BeautifulSoup as bs
import urllib2
from qgb import U,T
import re

s=open(r"D:\test\zys.html").read()
sp=bs(s,"html.parser" ) 

#class="in-reply-to ng-hide"report(comment)
# for j in sp.find_all(attrs={'class':"in-reply-to ng-hide"}):
	# j.decompose()  
for j in sp.find_all(attrs={'ng-if':"canReply(comment)"}):
	j.decompose()  
for j in sp.find_all(attrs={'ng-click':"report(comment)"}):
	j.decompose()  

sbr='<br><br><br><br><br><br><br><br><br><br><br><br>'
# open(r"D:\test\zys0.html",'wb').wite(sp.encode('gbk'))
im=0
ls=[]
for i in sp.find_all('li'):
	aurl,burl=None,None
	for j in i.find_all(attrs={"class":"comment-hd"}):
		urls = re.findall(T.REURL, str(j),re.I)
		if(0<len(urls)<3):
			aurl=urls[0]
			try:burl=urls[1]
			except:pass
			
			break
	if(burl!=None ):
		for k in ls:
			if(k[0][0]==burl):
				k.append([aurl,burl])
				break
			else:
				for ki in k:				
					if(ki[0]==burl):
						# ls.append()
						k.append([i])
		# ab=ls[ls.index([burl])]
		# U.msgbox(ab)
		
	else:ls.append([[aurl,burl]])
	# print aurl,burl
		
			
print ls
exit()




for i in sp.find_all(attrs={"class":"comment-body"},limit=344):
	name,href,rto=None,None,None
	# print i.text.encode('gbk')
	for j in i.find_all():
		# print j.get('class')
		if(str(j.get('class')).find(u'in-reply-to')>0):
			rto=j.find(attrs={"class":"ng-binding"})
			if(len(rto.text)<1):rto=None
			continue
			
		if(str(j.get('href')).find('http://www.zhihu.com/people/')!=-1):
			href=j.get('href');href=str(href)
			name=j.text.encode('gbk')
			continue
			# print name
			# if href not in ls:ls.append(href)
				
				
	print name,href,rto	
	ls.append((name,href,rto))
for j in ls :
	print j
	
print len(ls)
	# U.msgbox()
	# U.helphtml(i)