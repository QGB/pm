from bs4 import BeautifulSoup as bs
import urllib2
from qgb import U,T


s=open(r"D:\test\zys.html").read()
sp=bs(s,"html.parser" ) 
sp=bs(sp.encode("ascii"),"html.parser" ) 


# open('tmp.html','w').write()
U.setOut('BeautifulSoup.html')
print U.txthtml[0]
help(sp)
print U.txthtml[0]
U.resetOut()
print type(s)

