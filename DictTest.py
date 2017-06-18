d={'i': 4, 'j': 7}
da=d
da['i']=d
print d.keys()
print d['j']
print d['i']

da['k']=6
print d
print da
from sys import *
exit()

def r(a,i):
	i+=1
	if(i>22):return
	print i,a['i']
	r(a['i'],i)
	
r(d,0)