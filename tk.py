



import sys,time,os

print 2333
sys.stdout.flush()



from Tkinter import *
top=Tk()
b=Button(top,text='click')
b.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)

def foo(event):
	btn=event.widget
	btn['text']='clicked!'

b.bind('<Button>',foo)

top.mainloop()
