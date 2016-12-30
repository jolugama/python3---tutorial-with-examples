#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=536fB1qvSeE&index=22&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E22():
    ''' generadores
    Son funciones que nos permitirán obtener sus resultados poco a poco
    De este manera, nos permite iterar con filtros'''

    def __init__(self):
        pass

    def generador(self, *args):
        ''' generador que multiplica cada valor por 20'''
        for valor in args:
            yield valor * 20

    def generador2(self, *args):
        ''' generador que multiplica cada valor por 20 si es par
        si es impar indica no'''
        for valor in args:
            if valor % 2 == 0:
                yield valor * 20
            else:
                yield 'no'

    def generador3(self, *args):
        ''' generador con varios valores (devuelve tupla)
        si es par, mutiplica * 2, si inpar se pasa como negativo
        '''
        for valor in args:
            if valor % 2 == 0:
                yield valor * 2, True
            else:
                yield -valor, False

    def muestra(self):
        ''' muestra generador '''
        for valor in self.generador(1, 2, 3, 4, 5, 20, 40):
            print(valor)


    def muestra2(self):
        ''' muestra generador2 '''
        for valor in self.generador2(1, 2, 3, 4, 5, 20, 40):
            print(valor)

    def muestra3(self):
        ''' muestra generador3 '''
        for dato1, dato2 in self.generador3(1, 2, 3, 4, 5, 20, 40):
            print(dato1, dato2)


GEN = E22()
GEN.muestra()
print('###')
GEN.muestra2()
print('###')
GEN.muestra3()
