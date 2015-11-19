from bs4 import BeautifulSoup as bs
import urllib2
from qgb import U,T


# print U.pprint(globals())
# print U.calltimes(),U.calltimes(),U.calltimes()

# U.eval('''dicthtml('U.globals.html',globals())''')
# exec('''U.dicthtml('this.exec.globals.html',globals())''')
exit()

s=open(r"D:\test\zys.html").read()
sp=bs(s,"html.parser" ) 
sp=bs(sp.encode("ascii"),"html.parser" ) 



print 255