# -*- coding: utf-8 -*- 
import urllib2
import sys
from bs4 import BeautifulSoup
req = urllib2.Request("http://www.aizhan.com/siteall/www.ip138.com/")
f = urllib2.urlopen(req)
#content = f.read().decode('UTF-8').encode('GBK')  //网页抓取内容，显示中文正常
content = f.read()
soup = BeautifulSoup(content,"html.parser",fromEncoding="gb18030") #使用gb18030编码问题仍没解决
for gg in soup.findAll('div',{'class':'box_17'})[1]:
          print  gg