'''
Author = Mossein King
Alias = --Mk--

This script is open soure and of so open to editing and use as you wish
This script is dependent on socket module
This module provides access to the BSD socket interface. It is available on all modern Unix systems, Windows, MacOS, and probably additional platforms.  
'''
import socket

def main():	
	print connection_test()
	
def connection_test():
	locale = "www.google.com"
	try:
		host = socket.gethostbyname(locale)
    	# connect to the host
		s = socket.create_connection((host, 80), 2)
		connected = "Cheching internet access ... TRUE"
		return connected
	except:
		pass
		unconnected = "Cheching internet access ... FALSE\n Check your internet connection"
		return unconnected

if __name__ =='__main__':
	main()
