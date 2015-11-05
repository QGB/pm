import sys,time,os

from qgb import U

# d={'i':1,'j':2}
# print d['i']
# U.p(1,2,3)
# U.x()
# U.msgbox()
# print 2333
# sys.stdout.flush()



from Tkinter import *
top=Tk()
b=Button(top,text='click')
b.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)

def foo(event):
	btn=event.widget
	btn['text']='clicked!'
	U.pln( top.geometry())

b.bind('<Button>',foo)

U.pln(top.keys())
top['width']=222

top.mainloop()
