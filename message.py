
from socket import *
from threading import *
import time
from make_connection import *

commonport=1234
s = socket(AF_INET,SOCK_STREAM)

def communication(commonport,host_addr,user_name):
	def recieve(s,check_condition):
		while True:
			data,addr = s.recvfrom(1024)
			if(check_condition and data.decode('utf-8')=="Connection Required..!!"):
				print("********** %s CONNECTED SUCCESSFULLY **********"%(user_name))
				connection_req="Connection Required..!!"
				s.sendto(connection_req.encode('utf-8'),host_addr)
				check_condition=True
				continue
			print(data.decode('utf-8'))
	set_condition=True
	x=Thread(target=recieve,args=(s,set_condition))
	x.start()
	connection_req="Connection Required..!!"
	while True:
		message=input(" %s>> "%(user_name))
		s.sendto(messgae.encode('utf-8'),host_addr)



