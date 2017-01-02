#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=l7Aj6RhJx8g&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM&index=29
codigo facilito
'''

import sys


class E29():
    ''' pasar parámetros a los scripts '''

    def __init__(self):
        print(sys.argv)  # muestra los argumentos. el primero es el propio script

        if len(sys.argv) == 1:
            print('Es necesario añadir 3 argumentos')
        else:
            if sys.argv[1] == 'help':
                print('los argumentos son sumar o restar, seguido de 2 números')
            if len(sys.argv) > 3:
                self.operacion(sys.argv)

    def operacion(self, argumentos):
        ''' simple calculadora ejemplo con paso de argumentos '''
        resul = 0
        oper = argumentos[1:2]  #cojo el 2ºargumento, el operador
        numeros = argumentos[2:] #cojo el resto de argumentos, a partir del segundo
        for i in numeros:
            if oper[0] == 'sumar':
                resul += float(i)
            elif oper[0] == 'restar':
                resul -= float(i)
            else:
                resul = 'error'

        if resul != 'error':
            print('el resultado de {} es {}'.format(oper[0], resul))
        else:
            print('las operaciones son sumar y restar')


if __name__ == '__main__':
    E29()
