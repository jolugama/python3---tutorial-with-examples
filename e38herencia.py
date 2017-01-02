#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=SnqNoerkx0A&index=38&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''

''' ******
Clases padres que heredarán los hijos
****** '''
class Animal():
    ''' clase padre1 '''
    def __init__(self, mamifero, terrestre):
        self.mamifero = mamifero
        self.terrestre = terrestre

    @property
    def mamifero(self):
        '''devuelve True si es mamífero '''
        return self.mamifero

    @property
    def terrestre(self):
        '''devuelve True si es terrestre '''
        return self.terrestre


class Inteligencia():
    '''clase padre2'''
    def __init__(self, inteligente):
        self.inteligente = inteligente

    @property
    def inteligente(self):
        '''devuelve si es inteligente'''
        return self.inteligente



''' ******
Clases hijos
****** '''

class Perro(Animal, Inteligencia):
    '''clase hijo'''
    def __init__(self, mamifero, terrestre, inteligente):
        Animal.__init__(self, mamifero, terrestre)
        Inteligencia.__init__(self, inteligente)

    print('esto es un perro')


class Pez(Animal, Inteligencia):
    '''clase hijo'''
    def __init__(self, mamifero, terrestre, inteligente):
        Animal.__init__(self, mamifero, terrestre)
        Inteligencia.__init__(self, inteligente)

    print('esto es un pez')



PERRO1 = Perro(True, True, True)
print('perro1:: es mamifero:{}. es terrestre:{}'.format(PERRO1.mamifero, PERRO1.terrestre))
print('perro1:: es inteligente: {}'.format(PERRO1.inteligente))

PEZ1 = Pez(False, False, False)
print('pez1:: es mamifero:{}, es terrestre:{}'.format(PEZ1.mamifero, PEZ1.terrestre))
