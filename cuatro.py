# -*- coding: iso-8859-15 -*-
'''
Created on 22 sept. 2016

@author: Curso Ma�ana
4.- Hacemos un test.
Haces una pregunta con 5 intentos.
Pero la puntuaci�n ser� 5 si lo acierta a la primera...
y el resto, 4 3 2 1 
'''
def jugar(intento=5): 
    respuesta = raw_input("�De qu� color es una lim�n? ") 
    if respuesta != "amarillo": 
        if intento > 1: 
            print "Fallaste! Int�ntalo de nuevo\n" 
            intento -= 1 
            jugar(intento) # Llamada recursiva 
        else: 
            intento=0
            print "\nPerdiste! Puntos:", intento
    else:
        print "Acierto. Puntos:", intento
jugar()