from Tkinter import *
from math import *
from time import *
from random import *
from copy import deepcopy
from sys import *
from threading import *
import os


# w='qq\u0303aaa'
# print w
# exit()
class PrintFrame:
	def setIm(s,a):
		if(a<3):
			raise Exception('im<3')
		s.im=a

	def setBtn(s,im=8):
		if(im<>8):
			s.setIm(im)
		else:return
		s.w=1.0/s.im
		for i in range(s.im):
			s.b.append([])
			for j in range(s.im):
				s.b[i].append(Button(s.f))
				#bind i,j on btn
				
				s.b[i][j]['textvariable']={'i':i,'j':j}
				s.b[i][j].place(relwidth=s.w,relheight=s.w,rely=s.w*i,relx=s.w*j)
				s.b[i][j].bind('<Button>',s.bf)

	def bf(s,event):	
		b=event.widget
		# for ek in b.keys():
			# print ek,b[ek]
			
		print b['textvariable']
		sys.stdout.flush()
		# t= Toplevel(s.f)
		b.config(bg= 'white')
		pass

	def __init__(s,ast):
		s.f=Tk()
		s.b=[]
		s.im=8
		s.w=0
		s.setBtn()
		Thread(target=s.f.mainloop).start()

	def p(s,a):
		print type(s),type(a),len(a)
		# return
		for x in range(len(a)):
			for y in range(len(a[x])):
				s.b[x][y]['text']=str(a[x][y])



global gpf
gpf=PrintFrame('0')
gpf.setBtn(11)
# gpf=233
# #gpf.p(y)
# print gpf
# sys.exit()

def mp(a):
	print gpf

	try:
		raise Exception('111133333333333333311')
		print 244
	except Exception as err:
		print err

# mp(1)





