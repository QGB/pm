# from bs4 import BeautifulSoup as bs
# import urllib2
from qgb import U,T

# print file.__doc__

# s=help()
# U.x()

url=('http://www.zhihu.com/people/evenstar/answers?order_by=vote_num&page=15')

# s=urllib2.urlopen(url).read()
f=open('zhihues.html','r+')




U.resetOut()

U.x()
f.write('7656544')
f.flush()
# f.close()
# help(f)

f.re
print f.mode


# f.write(s)
# sp=bs(urllib2.urlopen(url).decode( 'utf-8'),"html.parser" ) 
# print(sp.prettify())
# print(sp.decode().encode('gb2312'))
#