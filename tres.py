# -*- coding: iso-8859-15 -*-
'''
Created on 22 sept. 2016

@author: Curso Mañana
3.- Calcula el total, subtotal y cuota de iva con funciones lambda
'''
subtotal= lambda subtotal: subtotal-(subtotal*0.21)
print "Subtotal:",subtotal(100)

iva= lambda iva: iva*0.21
print "IVA:",iva(100)

total =iva(100)+subtotal(100)
print "Total:",total