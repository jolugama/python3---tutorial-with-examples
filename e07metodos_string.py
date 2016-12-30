#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=I1a7piALq60&index=7&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E7:
    '''
    Métodos string en python.
    '''

    perro = 'Vito'
    lugar = 'casa'

    ''' FORMATO '''
    frase1 = 'El perro {a} está en {b}'.format(a=perro, b=lugar)
    frase2 = frase1.lower()
    frase3 = frase1.upper()
    frase4 = frase1.title()

    ''' BÚSQUEDA '''
    pos = frase1.find('Vito') #En la pos 9. Si -1=no encontrado. Igual que str.indexOf de javascript
    count = frase1.count('r') #cuenta las veces que concurre la letra r.
    frase1nuevo = frase1.replace('e', '-') #remplaza todos los e por -

    ''' TRANSFORMA EN LISTA '''
    frase1Lista = frase1.split(' ') #crea una lista de la frase y toma como separadores el indicado

    def __init__(self):
        print(self.frase1)
        print(self.frase2)
        print(self.frase3)
        print(self.frase4)

        print(self.pos)
        print(self.count)
        print(self.frase1nuevo)

        print(self.frase1Lista)


E7()

