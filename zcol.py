#coding=utf-8
from bs4 import BeautifulSoup as bs
import os,sys,re,urllib2,chardet
from qgb import U,T

def parser(ai):
	cmd='''curlt.bat %s'''%(ai)	
	os.system(cmd)
	
	s1=U.read('./zcol/%s.html'%ai)
	d=eval(s1)
	d=d['msg']
	
	im=d[0]
	d=d[1]
	d=d.replace('\/','/')
	
	exec('d=u{0}{1}{0}'.format("'"*3,d))
	
	return d
	# sp=bs(d,"html.parser" ) 
	# sa=sp.find_all('a')
	# print '='*44
	# print len(sa)
	# print sa[8].text
	# print d.keys()
	# U.write('sp.html',sp.)
	
parser(0)

exit()
i=-1
while(True):
	i+=1
	fn='%s.html'%i
	cmd='''curlt.bat %s'''%(i)	
	os.system(cmd)
	# exit()
	# if(os.path.getsize(fn)<5):i-=1;continue
	
	# sh=open(fn).read()
	# if(sh.find("answer-date-link-wrap")==-1):break
	
	U.pln(i) 
	if(i>16):exit()
exit()
i=0
while(True):
	st=''
	i+=1
	try:st=U.read('%s.json'%i)
	except:break
	exec('''st=%s'''%st)
	st=st['msg'][1]
	print i,st[233:311]
	U.helphtml(str(''))
	os.system('start http://www.qq.com/')
	exit()
	