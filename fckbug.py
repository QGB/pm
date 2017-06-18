# coding=utf-8
url='''http://218.196.43.18:8888/fckeditor/editor/filemanager/connectors/aspx/connector.aspx?Command=GetFoldersAndFiles&Type=File&CurrentFolder=d:/'''
from qgb import U,T
from urllib2 import *
import xml.etree.cElementTree as ET 
import chardet
import sys
reload(sys)
# sys.setdefaultencoding( 'ascii')

def getx(asu):
	sxml= urlopen(url).read()
	# U.write('fck.xml',sxml)
	sxml=U.read('fck.xml')
	sxml=sxml.decode('utf-8')
	print chardet.detect(sxml)
	return ET.fromstring(sxml)

x=getx(url)
# print u'ccsu\u6587\u6863\u8d44\u6599'
# exit()

# x.getchildren()[1].getchildren()[1].get('name')
def getd(ax):
	lx=ax.getchildren()[1].getchildren()
	for i in lx:
		sn=i.get('name')
		# sn=sn.encode('GB18030', 'ignore')
		print sn
		if sn.startswith('ccsu'):
			pass
		else:print chardet.detect(sn.encode('GB18030'))
			# sn=sn.decode('ISO-8859-2')
			# sn=sn.encode('utf-8')
			# print sn
			# print sn.encode('GB2312')
			
		# print .encode('GB18030', 'ignore')
# getd(x)
exit()
# print x[0].text
# U.helphtml(x[0])
sc='ccsu文档资料'
print chardet.detect(sc)
print type(sc)
# print isinstance(sc, unicode) 
# print sc.decode('gb2312')
# print dir(sc)
exit()
url+=sc
x=getx(url)
getd(x)

U.x()