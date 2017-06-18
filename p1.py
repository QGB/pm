from Tkinter import *
from threading import *
import threading,multiprocessing.dummy,time
from qgb import U,T



print U.getThreads()
U.x()
def p():
	for threadId, stack in sys._current_frames().items():
		print threadId
	U.pln()

def mp():
	while(True):
		p()
		time.sleep(2.5)

Thread(target=mp).start()

# exit()
# print threading.__all__ 
n1,n2=0,0
for i in range(2):
	U.pln(activeCount(),currentThread())
	t=Tk()
	b=Button(t,text='click')
	b.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)

	def foo(event):
		btn=event.widget
		btn['text']='clicked!'
		t=currentThread()
		U.pln(t)
		p()
		exit()
		# global n1,n2
		# if(str(t).find('d-2')>0):n2+=1
		# if(str(t).find('d-1')>0):n1+=1
		
		# U.pln(n1,n2)
		
	b.bind('<Button>',foo) 	
	Thread(target=t.mainloop).start()




	
exit()		
p()
