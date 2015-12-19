#coding=utf-8
gsuser='ze.ran'
gszhihu='https://www.zhihu.com/'
gszp=gszhihu+'people/'
gscmt0='''https://www.zhihu.com/node/AnswerCommentBoxV2?params=%7B%22answer_id%22%3A%22'''
gscmt1='%22%2C%22load_all%22%3Atrue%7D'
from bs4 import BeautifulSoup as bs
import os,sys,re,urllib2,chardet
from qgb import U,T
if(len(sys.argv)==2):
	if(len(sys.argv[1])>0):
		gsuser=sys.argv[1]
else:print 'Usage:',sys.argv[0],'zhihuUserUrl or id'
if(gsuser.find(gszp)>-1):
	gsuser=T.sub(gsuser,gszp,'').strip()
print 'Processing '+gsuser+' ....'

# U.mkdir('zhihu')
# os.chdir('zhihu')
# U.mkdir(gsuser)
# os.chdir(gsuser)

i=0
while(True):
	break
	i+=1
	fn='%s.html'%i
	url=gszp+gsuser+('/answers?page='+str(i))
	
	# U.pln(url) 
	# fh=open('%s.html'%i,'wb')
	# fh.write(urllib2.urlopen(url).read())
	# fh.close
	cmd='''Zcolcurl.bat %s'''%(i)
	# cmd=T.batencode(cmd)
	# print cmd
	os.system(cmd)
	# exit()
	# if(os.path.getsize(fn)<5):i-=1;continue
	
	# sh=open(fn).read()
	# if(sh.find("answer-date-link-wrap")==-1):break
	
	U.pln(i) 
	if(i>16):exit()

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
	