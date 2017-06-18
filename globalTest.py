class cc:
	def f(s):
		
		print g

	def ff(s):
		s.f()
from sys import *

# exit()
		
		
global g
g=11

c=cc()
c.ff()

print g