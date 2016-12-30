#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=ZqGynv-wgWg&index=5&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E5string:
    '''
    varias maneras de usar los string
    '''
    perro = 'vito'
    lugar = 'la casa'
    mensaje1 = 'el perro '+perro+' está junta a '+lugar
    mensaje2 = 'el perro %s está junto a %s' %(perro, lugar)
    mensaje3 = 'el perro {} está junto a {}'.format(perro, lugar)
    mensaje4 = 'el perro {1} está junto a {0} .... ups, parece que lo dije mal'.format(perro, lugar)
    #se puede indicar el orden, ejemplo en mensaje4

    def imprime(self):
        ''' primera '''
        print(self.mensaje1)


    def imprime2(self):
        ''' segunda '''
        print(self.mensaje2)

    def imprime3(self):
        ''' tercera '''
        print(self.mensaje3)

    def imprime4(self):
        ''' tercera, indicando el índice '''
        print(self.mensaje4)


E5 = E5string()
E5.imprime()
E5.imprime2()
E5.imprime3()
E5.imprime4()
