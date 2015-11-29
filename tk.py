import sys,time,os
from qgb import U
ls=[]

from Tkinter import *
top=Tk()
b=Button(top,text='click')
b.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)

def foo(event):
	btn=event.widget
	btn['text']='clicked!'
	btn['bg']='#008000'
	U.pln( top.geometry())

b.bind('<Button>',foo)

U.pln(top.keys())


top.mainloop()
