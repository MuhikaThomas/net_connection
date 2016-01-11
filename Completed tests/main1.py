'''
Author = Mossein King
Alias = --Mk--

This script is open soure and of so open to editing and use as you wish
This script is dependent on urllib module
This module provides a high-level interface for fetching data across the World Wide Web.
The module comes integrated in python
This method is unpreferable since urllib provides a high-level interface and hence  may not dedect very slow connections  
'''
import urllib

def main():
	if connection_try():
		print("Cheching internet access ... TRUE")
	else:
		print("Cheching internet access ... FALSE\n Check your internet connection")	
	
def connection_try():
	locale ='http://google.com'
	try:
		urllib.urlopen(locale)
		return True
	except:
		return False
		
if __name__ == '__main__':	
	main()


