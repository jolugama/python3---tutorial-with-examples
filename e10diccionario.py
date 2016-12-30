#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=_UELgsIxE7g&index=10&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E10:
    '''
    diccionario --> listas con índice y valor
    '''

    def __init__(self):
        diccionario = {'a': True, 'b': False, 34: 'valor'}
        print(diccionario)
        diccionario['a'] = False  # si está , lo modifica
        diccionario['zz'] = 'nuevo'  # si no está , se crea
        print(diccionario)
        print(diccionario['a'])  # muestro valor con lave 'a'
        try:
            print(diccionario['gggg'])  # va a dar error, no existe dicha clave
        except KeyError as err:
            print("KeyError, no existe key {0}".format(err))

        print('continua con la aplicación')
        '''
        una manera de evitar los try catch, cuando buscamos por valor,
        es mejor usar el método get de diccionario.
        devuelve valor de la id del primer parametro.
        devuelve el segundo valor si no se ha encontrado con esa id.
        '''
        print(diccionario.get('gggg', 'noEncontrado'))
        # ojo! abría que capturarlo con try, si no encuentra genera keyError
        del diccionario['a']
        print(diccionario)
        llaves = diccionario.keys()
        valores = diccionario.values()
        print(llaves)
        print(valores)
        # se fuerza a lista pura, para trabajar luego con ella
        llaves = list(diccionario.keys())
        valores = tuple(diccionario.values())  # se transforma en tupla
        print(llaves)
        print(valores)

        diccionario2 = {'dic2a': 33, 'dic2b': False}
        diccionario.update(diccionario2)
        print(diccionario)

E10()
