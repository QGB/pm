from bs4 import BeautifulSoup as bs
import urllib2,re
from qgb import U,T
s=open(r"D:\test\lby.html").read()
sp=bs(s,"html.parser" ) 

im=0
ls=[]
U.setOut('d:/test/dot/lby.dot')
print 'digraph G {'
for i in sp.find_all('li'):
	im+=1;si='_'+str(im);si=''
	aurl,burl=None,None
	for j in i.find_all(attrs={"class":"comment-hd"}):
		urls = re.findall(T.REURL, str(j),re.I)
		if(0<len(urls)<3):
			aurl=urls[0]
			try:
				if(len(urls[1])<1):break
				burl=urls[1]
			except:pass
			break
	aurl=T.sub(aurl,'/people/')
	burl=T.sub(burl,'/people/')
	aurl=si+aurl.replace('-','').replace('.','')

	
	if(burl!=None):
		burl=burl.replace('-','').replace('.','')
		print '%s->%s'%(aurl,burl)
	# else:
		# print aurl
	# ls.append((aurl,burl))
print '}'
U.resetOut()