#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=cJ9zcR1uTt8&index=19&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E19:
    '''
    Programación funcional - lambda.
    permite definir funciones mínimas, de una línea, sobre la marcha
    '''

    def __init__(self):
        mi_function = lambda valor_uno, valor_dos: valor_uno + valor_dos
        resultado = mi_function(40, 20)
        print(resultado)

        exclamacion = lambda sentencia: '¡¡¡¡{}!!!!'.format(sentencia)
        mi_exclamacion = exclamacion('vaya con las lambdas')
        print(mi_exclamacion)

E = E19()
