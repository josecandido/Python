# -*- coding: iso-8859-15 -*-
'''
Created on 22 sept. 2016

@author: Curso Mañana
'''
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close()          