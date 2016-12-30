#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=2KL-mJ4n1k4&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM&index=23
codigo facilito
'''


class E23():
    ''' Documentación
        Dispone de métodos para recoger la documentación, nombre de la funcion, etc.
    '''

    def __init__(self):
        pass

    def funcion1(self):
        ''' esta es la documentacion que dispone la funcion1.
        imprime en pantalla hola mundo
        '''
        print('Hola mundo')

    def funcion2(self, num1, num2):
        ''' esta es la documentacion que dispone la funcion2.
        retorna
        '''
        return num1 + num2

    #METADATAS (aparecerán si se escribe help(E23))
    __autor__ = 'jolugama'
    __copyrigth__ = 'GLP'
    __leches__ = 'leches ... ups'
    __maintainer__ = 'jose luis garcia'
    __email__ = 'joseluis@jolugama.com'
    __status__ = 'desarrollador'

DOCUMENTACION = E23
print(DOCUMENTACION.funcion1.__name__+ ':') #nombre de la funcion
print(DOCUMENTACION.funcion1.__module__)
print(DOCUMENTACION.funcion1.__doc__) #documentación de la funcion
print(DOCUMENTACION.__doc__) #documentación de la clase


'''
si desde consola escribimos
from e23docstring import E23
nos aparecerá su documentacion

si escribimos help(E23) nos aparecerá su documentación entera,
documentación de clase, funciones, y metadatas
o si solo queremos una función: help(E23.funcion1)
'''
