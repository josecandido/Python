# -*- coding: iso-8859-15 -*-
'''
Created on 22 sept. 2016

@author: Curso Mañana
5.- Crea una clase que gestione nominas
salario bruto=salaio base+cotizacion empresa+cotizacion trabajador
cotizacion empresa=salario*30%
cotizacion trabajador=salario*7.4%
salario neto=salario base - retencion irpf
si salario anual>50.000 retencion irpf es 25%
si es entre 30.000 y 50.000 irpf es 19%
si es menor que 30.000 es 15%
crea una clase para probar los metodos
'''

class gestion(object):
    def __init__(self,params):
        '''
        Constructor
        '''
        
    def bruto(self,salario):
        cotizacion_empresa=salario*0.3
        cotizacion_trabajador=salario*0.074
        salario_bruto=round(salario+cotizacion_empresa+cotizacion_trabajador,2)
        print "Salario bruto: ",salario_bruto
    
    def neto(self,salario):
        salario=salario*14
        if salario>=50000:
            irpf=salario*0.25
        elif salario>30000 and salario<50000:
            irpf=salario*0.19
        elif salario<30000:
            irpf=salario*0.15
        
        salario_neto=round(salario-irpf,2)
        print "Salario neto: ", salario_neto
    
class probar(object):
    total=gestion("params")#instanciar
    total.bruto(1000.2)
    total.neto(2500.2)
    
probar()