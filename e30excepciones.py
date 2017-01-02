#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=sNTowPB4YHI&index=30&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E30():
    ''' manejo de excepciones '''
    lista = [1, 5, 3]
    def __init__(self):
        self.control_errores('divideEntre0')
        self.control_errores('indexNoEncontrado')
        self.control_errores('generico')


    def control_errores(self, operacion):
        '''recibe un tipo de operacion y se espera que recoja el error'''
        try:
            if operacion == 'divideEntre0':
                print(2 / 0)
            elif operacion == 'indexNoEncontrado':
                print(self.lista[66])
            else:
                print(2+'h')
        except ZeroDivisionError as e_cero:
            print('error ZeroDivisionError: {}'.format(e_cero))
        except IndexError as e_index:
            print('error IndexError: {}'.format(e_index))
        except Exception as e_generico:
            print('error genérico: {}'.format(e_generico))

if __name__ == '__main__':
    E30()
