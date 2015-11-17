# coding=utf-8
from bs4 import BeautifulSoup as bs
from qgb import U,T
import urllib2

url=('http://www.zhihu.com/people/evenstar/answers?order_by=vote_num&page=15')

sp=bs(urllib2.urlopen(url),"html.parser" ,from_encoding = 'utf-8') 

help(bs)
#