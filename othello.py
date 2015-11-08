from threading import *
from Tkinter import *
from sys import *
from qgb import U,T

class gui:
#white 0 aw2, black 1 ab3,5 not,9 null
	def __im(s,a):
		if(a<3):
			raise Exception("a<3")
		s.im=a
		
	def onclick(s,event):
		b=event.widget
		btv=str(b['textvariable']).split(',')
		i=int(btv[0])
		j=int(btv[1])
		
		if(b['bg']=='green'):
			U.pln(i,j)
	#U.msgbox(i,c,btv)
		
	def setBtn(s,im=8):
		s.__im(im)		
		wf=min(s.im*32,700)
		s.fc.setfx(wf+10)
		wf=str(wf)
		s.f.geometry(wf+'x'+wf+'+1+-8')
		
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
		
		
		# print ia,w,w*64
	def update(s,ad=None):
		if(ad==None and s.da==None):
			raise Exception('da==none')
		if(ad!=None):
			s.da=ad
		if(s.im!=s.da.im):
			s.setBtn(s.da.im)
		
		for i in range(s.im):
			for j in range(s.im):
				if(s.da.y[i][j]==0):
					s.yb[i][j]['bg']='white'
				if(ad.y[i][j]==1):
					s.yb[i][j]['bg']='black'
				if(ad.y[i][j]==2):
					s.yb[i][j]['bg']='green'
				if(ad.y[i][j]==3):
					s.yb[i][j]['bg']='blue'
					
	class Fcontrol:
		def __init__(s,ss):
			s.f=Toplevel()
			w=0.3
			ir=0
			ic=0
			s.txtim=Text(s.f)
			s.txtim.place(rely=ir,relx=ic,relwidth=w,relheight=w-0.03)
			
			ir+=w
			s.bstart=Button(s.f,text='Start')
			s.bstart.place(rely=ir,relx=ic,relwidth=w,relheight=w)
			s.bstart.bind('<Button>',s.start)
			
			ic+=w
			s.bexit=Button(s.f,text='exit')
			s.bexit.place(rely=ir,relx=ic,relwidth=w,relheight=w)
			s.bexit.bind('<Button>',s.exit)
			
			
		def start(s,event):
			#print dir(s.txtim)
			print U.fields(s.txtim)
			U.pln( )
			
		
		def exit(s,event):
			U.x()
		
		def setfx(s,fx):
			s.f.geometry('66x66+'+str(fx)+'+248')
	def __init__(s,im=8):
		s.f=Tk()
		s.__im(im)
		if(s.im!=8):s.setBtn(s.im)
		
		
		s.fc=s.Fcontrol(s)
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
		s.c=0
		
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
						pass					
	def valid(s,colour,x,y):			
		#If there's already a piece there, it's an invalid move colour
		if s.y[x][y] in [1,0] :
			return False
		else:
			#Generating the list of neighbours
			neighbour = False
			neighbours = []
			for i in range(max(0,x-1),min(x+2,s.im)):
				for j in range(max(0,y-1),min(y+2,s.im)):
					if s.y[i][j] in [1,0]:
						neighbour=True
						neighbours.append([i,j])
			#If there's no neighbours, it's an invalid move
			if not neighbour:
				return False
			else:
				#Iterating through neighbours to determine if at least one line is formed
				valid = False
				for neighbour in neighbours:
					neighX = neighbour[0]
					neighY = neighbour[1]			
					#If the neighbour colour is equal to your colour, it doesn't form a line
					#Go onto the next neighbour
					if s.y[neighX][neighY]==colour:
						continue
					else:
						#Determine the direction of the line
						deltaX = neighX-x
						deltaY = neighY-y
						tempX = neighX
						tempY = neighY

						while 0<=tempX<=s.im1 and 0<=tempY<=s.im1:
							#If an empty space, no line is formed
							if s.y[tempX][tempY] not in [1,0]:
								break
							#If it reaches a piece of the player's colour, it forms a line
							if s.y[tempX][tempY]==colour:
								valid=True
								break
							#Move the index according to the direction of the line
							tempX+=deltaX
							tempY+=deltaY
				return valid

	def avail(s,c):
		for i in range(len(s.y)):
			for j in range(len(s.y[i])):
				if(s.valid(c,i,j)):
					s.y[i][j]=c+2
					U.pln(i,j)
	def aw(s):s.avail(0)
	def ab(s):s.avail(1)
	
	
	def turn(s,i,j):
		if(not s.valid(s.c,i,j)):
			return 
		
	def p(s):
		for i in range(len(s.y)):
			for j in range(len(s.y[i])):
				U.p(s.y[i][j],' ')
			print

			
			
			
d=da(22)
d.aw()
d.turn(1,3)

d.p()


g=gui()
g.update(d)


# print d.getround(0,0)
# U.msgbox()

# #print g.im
# g.setBtn(5)
