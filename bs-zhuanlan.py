# -*- coding: cp936 -*-
from bs4 import BeautifulSoup as bs
import urllib2
from qgb import U,T

U.helphtml(open(r"D:\test\zys.html"))
# print dir('645'),'645'.__len__
# help(U.x)



# print U.pprint(globals())
# print U.calltimes(),U.calltimes(),U.calltimes()

# U.eval('''dicthtml('U.globals.html',globals())''')
# exec('''U.dicthtml('this.exec.globals.html',globals())''')
exit()

s=open(r"D:\test\zys.html").read()
sp=bs(s,"html.parser" ) 

#class="in-reply-to ng-hide"report(comment)
# for j in sp.find_all(attrs={'class':"in-reply-to ng-hide"}):
	# j.decompose()  
for j in sp.find_all(attrs={'ng-if':"canReply(comment)"}):
	j.decompose()  
for j in sp.find_all(attrs={'ng-click':"report(comment)"}):
	j.decompose()  
	
open(r"D:\test\zys0.html",'wb').buffer.write(sp)
exit()
ls=[]

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