#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=XefbjfEDN-U&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM&index=6
codigo facilito
'''


class E6string2:
    '''
    obtener varias partes de un string, en javascript es mediante substring o substr.
    '''

    mensaje = 'En un lugar de la mancha, de cuyo nombre no quiero acordarme, ...'


    def __init__(self):
        print('1 '+self.mensaje)
        print('2 '+self.mensaje[:40]) #se toma por defecto, de 0 a 40
        print('3 '+self.mensaje[6:40])
        print('4 '+self.mensaje[-1]) #se imprime la ultima letra de la frase
        print('5 '+self.mensaje[::-1]) #se realiza un reverse de la frase
        print('6 '+self.mensaje[-14:]) #se imprime desde el final, la posicion 14, hasta el fin.
        print('7 '+self.mensaje[0:30:2]) #se imprime desde la 0 hasta la 30, de 2 en 2.





E6string2()

