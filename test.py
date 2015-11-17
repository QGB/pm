from sys import *
oldStdout,logfile = None,None 
try:  
    logfile = open('d:/1.log','w+')  
    oldStdout = stdout  
    stdout = logfile  
    print 'Hello World in File Log!'  
finally:  
    if logfile:logfile.close()  
    if oldStdout:stdout = oldStdout  
print 'Hello World in Screen! '
exit()

import threading,time
from qgb import U,T 

from sys import *

def f():
	x, y =U.getCursorPos()
	print x,y
	# U.p(x,y)
	U.pln(x,y)

def timer(t):
	while(True):
		# f()
		# U.p(U.getCursorPos())
		stdout.write("q")
		stdout.flush()
		time.sleep(t)
		

# timer(0.11)
print help(U.single)