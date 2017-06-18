import sys,os;sys.path.append('d:\pm');from qgb import *
from bs4 import BeautifulSoup as bs
import urllib2,re
sp='d:/test/kcn/'

def save(aurl):
	

r=urllib2.urlopen('http://g.cn')
print r.read()