# -*- coding: iso-8859-15 -*-
'''
Created on 22 sept. 2016

@author: Curso Mañana
1. Crea una función que muestre los números pares 
desde 0 a 500
tres hilos atacan a esta función.
el primero con un retraso de 2 segundos
el segundo de 3 segundos
y el tercero de 5 segundos
Cuando el hilo 2 llega el 22 se detiene. 
'''
import thread
import time


# Define a function for the thread
def pares(nombre,delay):
    i=0
    while i < 500:
        time.sleep(delay)
        i+= 1
        if nombre=="Hilo-2" and i==22:
            break
        if i%2==0:
            print "%s: %d" % (nombre, i)

# Create two threads as follows
try:
    thread.start_new_thread( pares, ("Hilo-1", 2, ) )
    thread.start_new_thread( pares, ("Hilo-2", 3, ) )
    thread.start_new_thread( pares, ("Hilo-3", 5, ) )
except:
    print "Error: unable to start thread"

while 1:
    pass