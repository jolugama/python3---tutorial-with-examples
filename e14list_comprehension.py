#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=Z-8Khdd2BUQ&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM&index=14
codigo facilito
'''


class E14:
    '''
    list comprehension: crear lista, diccionarios y tuplas de una manera sencilla.
    rellenar listas, tuplas y diccionarios en una sola linea
    '''

    def __init__(self):
        # metodo normal
        lista = []
        for valor in range(0, 101):
            lista.append(valor)
        print(lista)

        # mediante comprehension
        lista = [valor for valor in range(0, 101)]
        print(lista)

        # comprehension más complejos (en este caso solo los pares del 0 al 100)
        lista = [valor for valor in range(0, 101) if valor % 2 == 0]
        print(lista)

        # comprehension más complejos (en este caso solo los impares del 0 al 100)
        tupla = tuple(valor for valor in range(0, 101) if valor % 2 != 0)
        print(tupla)

        # comprehension más complejos (en este caso solo los impares del 0 al 100)
        diccionario = {indice:valor for indice, valor in enumerate(lista) if valor % 2 == 0}
        print(diccionario)
E14()
