#!/bin/python3

import sys
import socket
from datetime import datetime

#Define target
if len(sys.argv) ==2:
	target=socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalit amount of arguments!!")
	print("syantax: python3 scanner.py <ip>")
    sys.exit()

#Add a banner

print('#'*50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("@"*50)

try:
	for port in range(1,1000):
	    socket.setdefaulttimeout(1)
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result=s.connect_ex((target,port))
		if result ==0:
			print(f"Port {port} is open")
		s.close()
		
except KeyboardInterrupt:
	print("\n Exiting Program")
	sys.exit()
except socket.gaierror:
	print("\nHostname could not be resolved")
	sys.exit()
except socket.error:
	print("\nCould not connect to server")
	sys.exit()
