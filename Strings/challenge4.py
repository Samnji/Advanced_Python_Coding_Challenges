# Write a function to find the domain name from the IP address. 
# The function will accept an IP address, make a DNS request, 
# and return the domain name that maps to that IP address while using records of PTR DNS. 
# You can import the Python socket library.

import socket

def domainaNameResolver(ip_addr):
	host_name = socket.gethostbyaddr(ip_addr)

	return host_name[0]



ip_addr = input("Enter an ip address: ")

print(domainaNameResolver(ip_addr))