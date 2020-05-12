from os import *
import netifaces as ni
import time

def banner():
    print("*********************************************************")
    print("********************TERMINAL CHAT BOX********************")
    print("*********************************************************")

def screen_clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    banner()


def get_ip_addr():
    if name == 'nt':
        ip=input("[+] Enter your IP address  : ")
    else:
        ifaces=[]
        address=[]
        ip={}
        address=[ni.ifaddresses(iface)[ni.AF_INET][0]['addr'] for iface in ni.interfaces() if ni.AF_INET in ni.ifaddresses(iface)]
        for iface in ni.interfaces():
            if ni.AF_INET in ni.ifaddresses(iface):
                ifaces.append(iface)
        ip=dict(zip(ifaces,address))
        iface=input("[+] Enter your network interface which has connection : ")
        if iface in ifaces:
            print("[+] Your IP address in %s : %s"%(iface,ip[iface]))
            return ip[iface]	
        else:
            print("[+]Enter your interface properly.. (eg: eth0,wlan0,wlp2s0..) ")
            print("[+]Your interfaes are.." +str(ni.interfaces()))
            time.sleep(5)
            screen_clear()
            get_ip_addr()
	