#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=BJXCnAd6pdM&index=11&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E11:
    '''
    condicionales
    '''

    def __init__(self):
        fruta = 'manzana'
        # >   <   ==   !=   >=   <=
        if fruta == 'manzana':
            print('es una manzana')
        elif fruta == 'pera':
            print('es una pera')
        else:
            print('no es ni pera ni manzana')

        objeto = 'boli'
        mensaje = 'el objeto es lapiz' if objeto == 'lapiz' else 'no es un lapiz, si no un boli'
        print(mensaje)

        if fruta == 'manzana' or fruta == 'naranja':
            print('es una fruta, está claro')

E11()
