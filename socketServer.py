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
	while True:  #ѭ����ѯsocket״̬���ȴ�����    
		connection,address = sock.accept()    
		try:    
			connection.settimeout(50)  
			#���һ�����ӣ�Ȼ��ʼѭ������������ӷ��͵���Ϣ  
			''''' 
			���serverҪͬʱ���������ӣ������������Ӧ���ö��߳������� 
			����server��ʼ�����������while�����ﱻ��һ��������ռ�ã� 
			�޷�ȥɨ�������������ˣ������̻߳�Ӱ�����ṹ�����Լǵ�������������1ʱ 
			��������Ҫ��Ϊ���̼߳��ɡ� 
			'''  
			while True:  
				buf = connection.recv(4096)    
				print "Get value " +buf   
				print "send welcome"  
				connection.send('welcome to server!'+buf)    
				singleback(buf)
				U.p()
		except Exception as e:  #����������Ӻ󣬸��������趨��ʱ���������ݷ�������time out  
			 print e  
			 continue

		print "closing one connection" #��һ�����Ӽ���ѭ���˳������ӿ��Թص�  
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