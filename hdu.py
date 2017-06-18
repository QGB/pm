#coding=utf-8
from bs4 import BeautifulSoup as bs
import os,sys,re,urllib2
from qgb import U,T
import calendar
import datetime
d1 = datetime.datetime(1992, 6, 28)
def t(ai):
	dt=d1+ datetime.timedelta(hours=24*ai)
	return (dt.year,dt.month,dt.day)
i=0
while(True):
	i+=1
	# fh=open('%s.html'%i,'wb')
	# fh.write(urllib2.urlopen(url).read())
	# fh.close
	y,m,d=t(i)
	cmd='''stuID=12204105&realname="%"E5"%"82"%"85"%"E6"%"99"%"A8'''
	
	cmd='''curl "http://passport.redhome.cc/index.php/user/register" --data "red_email=ccsudata"%"40163.com&red_password=123qwe&red_repassword=123qwe&{4}&year={0}&month={1}&day={2}" >hdu\{3}.html'''.format(y,m,d,i,cmd)
	print '='*33,i
	os.system(cmd)
	# exit()
	# cmd=T.batencode(cmd)
	# print cmd
	
	# exit()
	# if(os.path.getsize(fn)<5):i-=1;continue
	
	# sh=open(fn).read()
	# if(sh.find("answer-date-link-wrap")==-1):break
	if(i>944):exit()
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
	