#coding=utf-8
gsuser='excited-vczh'
gszhihu='http://www.zhihu.com/'
gszp=gszhihu+'people/'
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

U.mkdir('zhihu')
os.chdir('zhihu')
U.mkdir(gsuser)
os.chdir(gsuser)

i=0
while(True):
	break
	i+=1
	fn='%s.html'%i
	url=gszp+gsuser+('/answers?page=%s'%i)
	
	fh=open('%s.html'%i,'wb')
	fh.write(urllib2.urlopen(url).read())
	fh.close
	
	sh=open('%s.html'%i).read()
	if(sh.find("answer-date-link-wrap")==-1):break
	
	U.pln(url) 
	# if(U.calltimes()>16):exit()
# exit()
import xlwt
wbook=xlwt.Workbook(encoding='GB18030')
ws =wbook.add_sheet('xlwt1')
def wrow(al,aws=None,aindex=-1):
	if(aws==None):global ws
	else:ws=aws
	if(ws==None and aws ==None):raise Exception('xlwt ws None')
	
	if(aindex>-1):im=aindex
	else:im=len(ws.rows)
	
	for i in range(len(al)):
		ws.write(im,i, al[i])
i=0
while(True):
	i=i+1
	sh=''
	try:sh=open('%s.html'%i).read()
	except:break
	sp=bs(sh,"html.parser" ) 
	qs=sp.find_all('div',attrs={'class':'zm-item'})
	for qi in qs:
		ti=qi.find('a',attrs={'class':'question_link'})
		tiu=gszhihu+T.sub(ti,'''href="/''','''">''')
		ti=ti.text.encode('GB18030','ignore')
		
		vote=qi.find('a',attrs={'class':'zm-item-vote-count js-expand js-vote-count'}).text
		ci=qi.find('textarea',attrs={'class':'content hidden'})
		if(ci==None):
			sci=qi.prettify().encode('GB18030','ignore')
			spt=T.sub(sci,'answer-date-link meta-item','''/a>''')
			spt=T.sub(spt,'>','''<''')
			sci='!!!qgb!!!回答建议修改'
			wrow(['vote','cmt',spt,'set','ti','len(ti)','tiu',len(sci),sci])
			continue
		else:
			ci= ci.prettify().encode('GB18030','ignore')
			sci=T.sub(ci,'','''<span class="answer-date-link-wrap">''')
			sci=T.sub(sci,'''<textarea class="content hidden">''')
			
		def getday(a):
			'''pt et'''
			a=str(a)
			days = re.findall("20[0-9]{2}-[0-9]{2}-[0-9]{2}", a,re.I)
			ild=len(days)
			if(ild<1 or ild >2):
				return T.sub(a,'''">''','''</a>'''),''
				# raise Exception('days :'+a)
			if(ild==1):return days[0],''
			return days[0],days[1]
		spt,set=getday(T.sub(ci,'''<span class="answer-date-link-wrap">''','</span>'))

		cmt=qi.find('a',attrs={'class':' meta-item toggle-comment'}).text.encode('GB18030','ignore')
		cmt=T.sub(cmt,'',' ').strip()
		
		print '-'*60
		print vote,cmt,spt,set,ti,tiu,sci[:6]
		wrow([vote,cmt,spt,set,ti,len(ti),tiu,len(sci),sci[:32760]])
	# exit()

# print(sp.text.encode('utf-8').decode('gbk'))

# print ws.rows
os.chdir('..')
wbook.save(gsuser+'.xls')