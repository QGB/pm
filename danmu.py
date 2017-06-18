import sys,time,os
from qgb import U
ls=[]

from Tkinter import *
top=Tk()
b=Button(top,text='click')
b.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)
# b.attribute("-alpha", 0.9)
# U.helphtml(b)

def foo(event):
	btn=event.widget
	btn['text']='clicked!'
	btn['bg']='#008000'
	U.pln( top.geometry())
b.bind('<Button>',foo)

cv = Canvas(top,bg = 'white')
cv.create_rectangle(10,10,110,110,
                    outline = 'red',
                    dash = 10,
                    fill = 'green')
cv.pack()

top.wm_attributes('-topmost',1)
top.attributes("-alpha", 0.5)
top.mainloop()
