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
ls=[]
U.setOut('d:/test/dot/z.dot')
print 'digraph G {'
for i in sp.find_all(attrs={"class":"comment-hd"},limit=344):
	name,href,rto=None,None,None
	# print i.text.encode('gbk')
	for j in i.find_all():
		# print j.get('class')
		if(str(j.get('class')).find(u'in-reply-to')>0):
			rto=j.find(attrs={"class":"ng-binding"})
			# rto=rto.get('href')
			# rto=str(rto)
			if(len(rto)<1):rto=None
			continue
			
		if(str(j.get('href')).find('http://www.zhihu.com/people/')!=-1):
			href=j.get('href');href=str(href)
			name=j.text.encode('gbk')
			continue
			# print name
			# if href not in ls:ls.append(href)
				
	href=T.sub(href,'/people/')
	rto=T.sub(rto,'/people/')
	href=href.replace('-','').replace('.','')
	
	
	if(rto!=None):
		rto=rto.replace('-','').replace('.','')
		print '%s->%s'%(href,rto)
	else:
		print href
	ls.append((href,rto))
print '}'
U.resetOut()
for j in ls :
	print j
	
# print len(ls)
	# U.msgbox()
	# U.helphtml(i)