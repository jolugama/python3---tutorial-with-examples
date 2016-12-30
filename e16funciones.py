#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=vMTV0hY2jio&index=16&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''
GLOBAL_VARIABLE = 3


class E16:
    '''
    funciones
    '''

    def __init__(self):
        pass

    def suma(self, valor_uno, valor_dos):
        ''' función con 2 argumentos'''
        return valor_uno + valor_dos

    def multiplicacion(self, valor_uno, valor_dos=5):
        ''' se puede asignar un argumento, como valor por defecto '''
        return valor_uno * valor_dos

    def suma2(self, valor_uno, valor_dos):
        ''' se puede returnar varios valores, lo hace en formato tupla por defecto '''
        return valor_uno + valor_dos, valor_uno, valor_dos

    def mostrar_resultado(self, funcion):
        ''' pasar funciones dentro de funciones '''
        print(funcion(6, 8))

    def cambio_variable_global(self):
        ''' se puede cambiar el valor de una variable global '''
        global GLOBAL_VARIABLE
        GLOBAL_VARIABLE = 10

E = E16()
print(E.suma(20, 9))
print(E.multiplicacion(2))
print(E.suma2(20, 9))

# multiples variables para recibir una funcion de multiples returnos
VAL1, VAL2, VAL3 = E.suma2(20, 9)
print('la suma de {} + {} es igual a {}'.format(VAL2, VAL3, VAL1))


# asigno a una variable la funcion multiplicacion
# llamo a mostrar resultado cuya funcion es argumento.
print('....')
TMP = E.multiplicacion
E.mostrar_resultado(TMP)
print('....')


print(GLOBAL_VARIABLE)
E.cambio_variable_global()
print(GLOBAL_VARIABLE)
