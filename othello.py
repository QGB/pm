from threading import *
from Tkinter import *
from sys import *
from qgb import U,T

class gui:
#white 0 2, black 1 3,5 not,9 null
	def __im(s,a):
		if(a<3):
			raise Exception("a<3")
		s.im=a
		
	def onclick(s,event):
		b=event.widget
		btv=b['textvariable']
		btv=str(btv).split(',')
		i=int(btv[0])
		j=int(btv[1])
		b['bg']='green'
		if(i==0):
			b['bg']='black'
		if(j==0):
			b['bg']='white'
		
		# j=b['textvariable']['j']
		# print b['bg'],type(b['bg'])
		U.pln(i,j)
		U.pln(s.f.geometry())
	#U.msgbox(i,c,btv)
		
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
				b['textvariable']=str(i)+','+str(j)						
				b.bind('<Button>',s.onclick)
				
		s.f.geometry('793x724+1+-24')
		# print ia,w,w*64
	def __init__(s,im=8):
		s.f=Tk()
		s.setBtn(im)
		Thread(target=s.f.mainloop).start()

class da:
	def __init__(s,im):
		s.im=im
		s.im1=im-1
		i2=(s.im/2)
		s.y=[]
		for i in range(s.im):
			s.y.append([])
			for j in range(s.im):
				s.y[i].append(5)#text=str(i)+','+str(j) 
			s.y[i].append(9)#list[-1] is last
			
		
		s.y[i2-1][i2-1]=0
		s.y[i2][i2-1]=1
		s.y[i2-1][i2]=1
		s.y[i2][i2]=0
		

		s.y.append([9 for i in range(s.im+1)])
		
	def init(s):
		pass
	#im
	def getround(s,i,j):
		r=[]
		ri=9
		try:r.append(s.y[i-1][j])
		except:r.append(ri)
		try:r.append(s.y[i-1][j+1])
		except:r.append(ri)
		try:r.append(s.y[i][j+1])
		except:r.append(ri)
		try:r.append(s.y[i+1][j+1])
		except:r.append(ri)
		try:r.append(s.y[i+1][j])
		except:r.append(ri)
		try:r.append(s.y[i+1][j-1])
		except:r.append(ri)
		try:r.append(s.y[i][j-1])
		except:r.append(ri)
		try:r.append(s.y[i-1][j-1])
		except:r.append(ri)
		return r
	def near(s,ac):
		for i in range(s.im):
			for j in range(s.im):
				c=s.y[i][j]
				if(c==ac):
					for k in getround(i,j):
						
	def aw(s):
		pass
	
	def p(s):
		for i in range(len(s.y)):
			for j in range(len(s.y[i])):
				U.p(s.y[i][j],' ')
			print


d=da(22)
# #
d.aw()
d.p()
# print d.getround(0,0)
# U.msgbox()
#g=gui(33)
# #print g.im
# g.setBtn(5)
