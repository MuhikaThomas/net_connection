'''
Author = Mossein King
Alias = --Mk--

This script is open soure and of so open to editing and use as you wish
This script is dependent on httplib module
This module defines classes which implement the client side of the HTTP 	and HTTPS protocols. It is normally not used directly — the module 		urllib uses it to handle URLs that use HTTP and HTTPS.

It will be faster to just make a HEAD request so no HTML will be fetched.
Also I am sure google would like it better this way

https://docs.python.org/2/library/httplib.html
'''
import httplib

def main():
	if connection_test():
		print("Cheching internet access ... TRUE")
	else:
		print("Cheching internet access ... FALSE\n Check your internet connection")
	
def connection_test():
	host = "www.google.com"
	connection = httplib.HTTPConnection(host)
	try:
		connection.request("HEAD", "/")
		return True
	except:
		return False
	
if __name__ == '__main__':
	main()		
