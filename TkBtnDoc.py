# import qgb

from Tkinter import *
from qgb import *


U.cd('/pm/qgb')
U.cmd('pwd')
U.cmd('rm *.pyc')
U.cmd('ls')
exit()
# The image must be stored to Tk or it will be garbage collected.
# top.image = tk.PhotoImage(file='bg.jpg')
top=Tk()

top.geometry("222x222+250+250")

label = Label(top, bg='red')
# U.helphtml(label)
# exit()
label.place(relwidth=1,relheight=1)

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


top.overrideredirect(True)
top.lift()
top.wm_attributes("-topmost", True)
# top.wm_attributes("-disabled", True)
# top.wm_attributes("-transparentcolor", "blue")
label.pack()

top.mainloop()
