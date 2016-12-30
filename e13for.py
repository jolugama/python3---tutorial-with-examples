#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=aqnjB3dydik&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM&index=13
codigo facilito
'''


class E13:
    '''
    for
    '''

    def __init__(self):
        lista = [11, 22, 33, 44, 55, 66, 77, 88, 99]
        tupla = ('inicio de tupla', 1, 6, 7, 9, 4, 3, 2, 'fin de tupla')
        for valor in lista:
            print(valor)

        for valor in tupla:
            print(valor)

        # si solo pongo un parametro, empieza desde 0. si 3 parametros, es el n
        # de saltos
        nuevo_rango = range(0, 10)
        for valor in nuevo_rango:
            print(valor)

        # mediante enumerate, si dispone de indice y valor
        for indice, valor in enumerate(lista):
            print('indice {} cuyo valor es {}'.format(indice, valor))

        # mediate range
        for valor in range(0, len(lista)):
            print(valor)

        # recorrer un diccionario por items, values o keys
        diccionario = {'a': 11, 'b': 22, 'c': 33}
        for identificador, valor in diccionario.items():
            print('el identificador {} tiene el valor de {}'.format(identificador, valor))
E13()
