# -*- coding: cp936 -*-
from bs4 import BeautifulSoup as bs
import urllib2
from qgb import U,T

# U.helphtml(U.x)
# print dir('645'),'645'.__len__
# help(U.x)



# print U.pprint(globals())
# print U.calltimes(),U.calltimes(),U.calltimes()

# U.eval('''dicthtml('U.globals.html',globals())''')
# exec('''U.dicthtml('this.exec.globals.html',globals())''')
# exit()

s=open(r"D:\test\zys.html").read()
sp=bs(s,"html.parser" ) 

#class="in-reply-to ng-hide"report(comment)
for j in sp.find_all(attrs={'class':"in-reply-to ng-hide"}):
	j.decompose()  
for j in sp.find_all(attrs={'ng-if':"canReply(comment)"}):
	j.decompose()  
for j in sp.find_all(attrs={'ng-click':"report(comment)"}):
	j.decompose()  
	
ls=[]
for i in sp.find_all(attrs={"class":"comment-body"}):
	# print i.text.encode('gbk')
	for j in i.find_all():
		href=j.get('href');href=str(href)
		if(href.find('http://www.zhihu.com/people/')!=-1):
			sn= j.text.encode('gbk')
			if href not in ls:
				ls.append(href)
				
				
				
for j in ls :
	print j
	# U.msgbox()
	# U.helphtml(i)