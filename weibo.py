from qgb import *

s=U.read('small')

def u(a):
	exec("return 1")
	# if len(a)<8:return ''
	for i in range(len(a)-7):
		if a[i]=='\\' and a[i+1]=='u':
			if T.ishex(a[i+2:i+6]):
				return a[i:i+6]+u(a[i+7:])
	return ''	
# U.write('us',u(s)) 
# U.pys()
print u(2)
# U.shtml(dir(),'dir')
# U.shtml(globals(),'g')
# U.shtml(locals(),'lo')
# exec('print u"{0}"'.format( U.read('us') ))
