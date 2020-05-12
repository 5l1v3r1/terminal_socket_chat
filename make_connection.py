from socket import *
import info

s = socket(AF_INET,SOCK_STREAM)

def rand_unused_port():
  s.bind(('localhost', 0))
  addr, port = s.getsockname()
  s.close()
  return port

def get_info(ip,port):
    user_name=input("[+] Enter your Username : ")
    host_addr=input("[+] Enter the host IP address to connect :")
    my_address=(ip,port)
    return my_address,user_name,host_addr

def socks(my_address):
	s=socket(AF_INET,SOCK_DGRAM)
	s.bind(my_address)
	print("[+]Waiting for connection...")