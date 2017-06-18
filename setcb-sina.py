import sys,time,os
from qgb import U,T,clipboard as cb
ls=U.read('d:/qgbkeyset.txt').split('\n')
# U.pprint(ls) 
# exit()

from Tkinter import *
top=Tk()
def foo(event):
	btn=event.widget
	s=btn['text']
	U.pln(s )
	cb.set(s)


lb=[]
i=0
for si in ls:
	if(len(si)<3):continue
	b=Button(top,text=si)
	ih=20
	b.place(relx=((i%5*1.0)/5), y=0, relwidth=0.2, height=ih)
	b.bind('<Button>',foo)
	i+=1

top.geometry("%dx%d+%d+%d" % (333,111,11,333,))
top.mainloop()
