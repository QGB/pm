# -*- coding: cp936 -*-  
from Tkinter import *
from PIL import ImageGrab,ImageTk
from qgb import U,T
import os,sys,socket
'''
620,0
1113,259
'''
def muti():    
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
	sock.connect(('localhost', 2233))
	import time    
	flag = 0
	while True:   
		time.sleep(3)    
		sock.send('send to server with value: '+ '%d'%flag )    
		print sock.recv(4096)   
		flag+=1#change to another type of value each time  
	sock.close()    


muti()
U.x()

def singleback(msg):
	U.msgbox(msg)
	
U.single(port=2233,callback=singleback)
	
U.x()
try:os.open('your_lockfile',os.O_CREAT|os.O_EXCL|os.O_RDWR)
except Exception as e:U.msgbox(e.errno)

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
top.mainloop()