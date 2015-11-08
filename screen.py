# -*- coding: cp936 -*-  
from Tkinter import *
from PIL import ImageGrab,ImageTk
from qgb import U,T
import os,sys,socket
'''
620,0
1113,259
'''
io=0
def singleback(msg):
	global io
	U.pln(io)
	io+=1
	#U.pln(top)
	if(io<5 or io>2):raise Exception()
	if(msg==U.SG_ASK):
		U.msgbox(msg)
	
if(U.isingle(2233)):
	U.single(port=2233,callback=singleback)
else:U.x()


		#U.x()
	

help(ImageGrab.grab)


w, h = 1113-620,259
img = ImageGrab.grab((620,0,1113,259))

top=Tk()
top.geometry('333x333+55+444')

img=ImageTk.PhotoImage(image=img)
background_label = Label(top, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)




top.geometry("%dx%d+%d+%d" % (w,h,0,800-h-20))

lb=Label(top,text='76543')
lb.place(x=0,y=0,relheight=0.1,relwidth=0.1)


xmin=1368;xmax=0;ymin=1368;ymax=0
lr=[]
def foo(event):
	global xmin,xmax,ymin,ymax

	x,y=event.x_root,event.y_root
	xmax,ymax=max(x,xmax),max(y,ymax)
	xmin,ymin=min(x,xmin),min(y,ymin)
	lb['text']=str((xmin,ymin))+'\n'+str((xmax,ymax))

	
top.bind('<Button>',foo)
top
top.mainloop()