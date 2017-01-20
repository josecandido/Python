# -*- coding: iso-8859-15 -*-
'''
Created on 22 sept. 2016

@author: Curso Mañana
2. Crea un socket de cliente y servidor.
El cliente se conecta al servidor y nos debe indicar:
el nombre del servidor al que se ha conectado y su puerto.
la completa de conexión.
'''
import socket

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
print host
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    #print 'Conexion de:', addr
    c.send('Nombre del servidor: '+ host+ ' Puerto: '+ str(port))
    c.close()              