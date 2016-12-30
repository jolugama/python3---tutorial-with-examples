#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=I1a7piALq60&index=7&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E8:
    '''
    Listas, los arrays en javascript
    '''

    def __init__(self):
        mi_lista = ['una string', 4.2, 56, False]
        print(mi_lista)
        mi_lista.append('otro') #añado string al final de la lista
        print(mi_lista)
        mi_lista.insert(1, 'otro string') #inserto un string en la posición 1
        print(mi_lista)
        mi_lista.remove(4.2) #quita todos los que tengan como valor 4.2
        print(mi_lista)
        ultimo_lista = mi_lista.pop() #quita el último de la lista
        print(ultimo_lista)
        print(mi_lista)
        mi_lista2 = [5, 9, 44, 4, 2, 1, 5, 7, 4, 3, 23, 66]
        print(mi_lista2)
        mi_lista2.sort() #ordeno lista
        print(mi_lista2)
        mi_lista2.reverse() #ordeno lista en sentido inverso
        print(mi_lista2)
        mi_lista.extend(mi_lista2) #uno dos listas
        print(mi_lista)

E8()
