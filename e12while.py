#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=u6Hqs0bL_Ew&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM&index=12
codigo facilito
'''


class E12:
    '''
    while
    '''

    def __init__(self):
        contador = 0
        while contador < 10:
            print(contador)
            contador += 1
        else:
            print('el while ha terminado')



        contador = 0
        bandera = True
        while bandera:
            print(contador)
            contador += 1
            if contador == 5:
                continue
            elif contador == 7:
                break

E12()
