from multiprocessing import *
from Tkinter import *
from sys import *
def sf():
    print 233
	#Tk().mainloop()

p=Process(target=sf)
p.start()
p.join()
