#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=c9J7FHLjBds&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM&index=21
codigo facilito
'''


class E21(object):
    ''' mi clase decorador
    Añade funcionalidad extra a una función'''

    def __init__(self, func):
        print('__init__()')
        func()

    def __call__(self):
        print('__call__()')



############### sin decoradores ###############
print('''
sin decoradores
''')
def funcion():
    '''funcion sin decorar'''
    print('funcion()')




print('Inicio')
DECORADO = E21(funcion)
DECORADO()
print('Fin')



############### con decoradores ###############
print('''

con decoradores
''')
@E21
def funcion2():
    '''funcion a la que vamos a decorar '''
    print('funcion2()')




print('Inicio')
funcion2()
print('Fin')



############### otro ejemplo, suma y resta con decoradores ###############
print('''

decoradores, otro ejemplo suma y resta
''')
def logger(func):
    ''' funcion decoradora '''
    def box(*args, **kwargs):
        ''' wrapper '''
        print('los argumentos son: {}, {}'.format(args, kwargs))
        result = func(*args, **kwargs)
        return result
    return box

@logger
def suma(num1, num2):
    ''' suma argumentos '''
    return num1+num2

@logger
def resta(num1, num2):
    ''' resta argumentos '''
    return num1 - num2

print(suma(3, 2))
print(resta(3, 2))

# información obtenida de:
# http://www.3engine.net/wp/2015/02/decoradores-python/


