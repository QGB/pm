# -*- coding: cp936 -*-  
import os,sys,socket
from qgb import U,T



def singleback(msg):
	#U.pln(msg)
	U.msgbox(msg)
	print msg
	U.p()
	
def test():
	sock=None
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
	sock.bind(('localhost', 8001))
	sock.listen(5) 
	print "Server is listenting port 8001, with max connection 5"   
	while True:  #循环轮询socket状态，等待访问    
		connection,address = sock.accept()    
		try:    
			connection.settimeout(50)  
			#获得一个连接，然后开始循环处理这个连接发送的信息  
			''''' 
			如果server要同时处理多个连接，则下面的语句块应该用多线程来处理， 
			否则server就始终在下面这个while语句块里被第一个连接所占用， 
			无法去扫描其他新连接了，但多线程会影响代码结构，所以记得在连接数大于1时 
			下面的语句要改为多线程即可。 
			'''  
			while True:  
				buf = connection.recv(4096)    
				print "Get value " +buf   
				print "send welcome"  
				connection.send('welcome to server!'+buf)    
				singleback(buf)
				U.p()
		except Exception as e:  #如果建立连接后，该连接在设定的时间内无数据发来，则time out  
			 print e  
			 continue

		print "closing one connection" #当一个连接监听循环退出后，连接可以关掉  
		connection.close()   




def t(f,m):
	f(m)
	
from threading import *

# t(singleback,65432)	

# Thread(target=t,args=[singleback,65432]).start()

print U.isingle(2233)
U.single(port=2233,callback=singleback)

print U.isingle(2233)
U.pln(U.__mm)