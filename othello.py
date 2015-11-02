from threading import *
from Tkinter import *
from sys import *
from qgb import U,T

class gui:
	def __im(s,a):
		if(a<3):
			raise Exception("a<3")
		s.im=a
		
	def onclick(s,event):
		b=event.widget
		print b['textvariable'][i]
		# j=b['textvariable']['j']
		#U.p(66)
		U.msgbox()
		
	def setBtn(s,im=8):
		s.__im(im)
		w=1.0/s.im
		s.yb=[]
		for i in range(s.im):
			s.yb.append([])
			for j in range(s.im):
				s.yb[i].append(Button(s.f,))#text=str(i)+','+str(j) 
				b=s.yb[i][j]
				b.place(relx=j*w,rely=i*w,relwidth=w,relheight=w)
				b['textvariable']={'i':i,'j':j}
				b.bind('<Button>',s.onclick)
		#print s.yb
	def __init__(s,im=8):
		s.__im(im)
		s.f=Tk()
		Thread(target=s.f.mainloop).start()
g=gui()

print g.im
g.setBtn(4)
