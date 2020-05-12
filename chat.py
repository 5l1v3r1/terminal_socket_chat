from info import *
from make_connection import *
from message import *


if(__name__=="__main__"):
	screen_clear()
	ip=get_ip_addr()
	port=rand_unused_port()
	my_address,username,host_address=get_info(ip,port)
	socks(my_address)
	communication(commonport,host_address,username)
    