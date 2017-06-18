# -*- coding: cp936 -*-  
from Tkinter import *
from threading import *
from PIL import ImageGrab,ImageTk
from qgb import U,T
import os,sys,socket,time,threading
'''
620,0
1113,259
'''

x0=0;y0=0
def loop():
	while(True):
		# U.msgbox(1)
		time.sleep(0.09)
		global top,tbg,iw,x0,y0
		x,y=U.getCursorPos()
		if(x==x0 and y==y0):
			time.sleep(0.1)
			# U.pln(x,y)
		x0=x;y0=y
		if(y>299+30 or x<620-30):
			# img= ImageGrab.grab((0+6,800-iw*2+6,iw*2,800))
			# img=ImageTk.PhotoImage(image=img)
			tbg['image'] =''
			# top.lower()
			time.sleep(0.1)
			continue
		# exit()
		
		# U.msgbox(2)
		img= ImageGrab.grab((x-iw,y-iw,x+iw,y+iw))
		img=ImageTk.PhotoImage(image=img)
		tbg['image'] =img 
		# top.lift()
		# U.msgbox(4)
		

# exit()
# loop()
# import pdb 
# pdb.set_trace() 


io=0
def singleback(msg):
	global io,top
	io+=1
	if(io%2==0):top.lower()
	else:top.attributes('-topmost',1)
	
	
	


# U.x()
if(U.notsingle(2233)):U.x(msg='twice')


		#U.x()
	
U.single(port=2233,callback=singleback)
# help(ImageGrab.grab)


w, h = 1113-620,259
img = ImageGrab.grab((620,0,1113,259))



		
top=Tk()


img=ImageTk.PhotoImage(image=img)
tbg = Label(top)
tbg.place(x=0, y=0, relwidth=1, relheight=1)
# tbg['image'] =img
# help(top)
# U.x()

iw=99
w=iw*2
top.geometry("%dx%d+%d+%d" % (w,w,1280-w,800-w))
top.attributes('-topmost',1)

lb=Label(top,text='')
lb.place(relx=0.48,rely=0.48,relheight=0.04,relwidth=0.04)
lb['bg']='red'

# print U.methods(top)

xmin=1368;xmax=0;ymin=1368;ymax=0
lr=[]
def foo(event):
	global xmin,xmax,ymin,ymax
	
	x,y=event.x_root,event.y_root
	xmax,ymax=max(x,xmax),max(y,ymax)
	xmin,ymin=min(x,xmin),min(y,ymin)
	lb['text']=str((xmin,ymin))+'\n'+str((xmax,ymax))
	
	U.pln(activeCount())
	# U.x()
	
	Tk().mainloop()
	
	

# sleep(1)
top.bind('<Button>',foo)

# def fk(event):
	# print U.methods(event)
	# U.pln()
# top.bind('<Control-F1>',foo)

Thread(target=loop).start()

top.mainloop()
U.x()