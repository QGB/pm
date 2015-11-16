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