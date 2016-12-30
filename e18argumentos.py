#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=PeWKpuFpGZA&index=18&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E18:
    '''
    argumentos
    '''

    def __init__(self):
        pass

    def suma(self, *args):
        ''' al tener * se puede poner x argumentos, todos se recogen en una tupla
        Aunque args se puede llamar de cualquier nombre, en python indican llamarlo así'''
        print(args)
        resultado = 0
        for valor in args:
            resultado += valor
        return resultado
 
    def suma2(self, **kwargs):
        ''' al tener doble **, se puede poner x argumentos. se recoge como diccionario
        Aunque kwargs se puede llamar de cualquier nombre, se debe llamar así'''
        print(kwargs)
        resultado = 0
        for valor in dict(kwargs).values():
            resultado += valor
        return resultado

E = E18()
RESULT = E.suma(1, 4, 8, 5, 4, 8, 4, 2)
print(RESULT)

RESULT2 = E.suma2(uno=1, dos=23, tres=5)
print(RESULT2)
