import sys,time,os
from qgb import *
ls=[]

from Tkinter import *
top=Tk()
b=Button(top,text='click')
b.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)
# b.attribute("-alpha", 0.9)

def foo(event):
	U.pause()
	btn=event.widget
	btn['text']='clicked!'
	btn['bg']='#008000'
	U.pln( top.geometry())

b.bind('<Button>',foo)


# top.wm_attributes('-topmost',1)
# top.attributes("-alpha", 0.4)
top.mainloop()
