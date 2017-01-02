#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=QP4vJg8q-ZA&index=37&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E37Circulo():
    '''clase círculo. metodos estáticos'''
    # _pi = 3.14159

    @staticmethod
    def constant_pi():
        '''Método estático. es de la clase y no de cada instancia.
        un mismo método para x objetos que se creen'''
        return 3.14159


    def __init__(self, radio):
        self.radio = radio

    def area(self):
        '''calcula area de un círculo'''
        return self.radio * self.radio * self.constant_pi()



if __name__ == '__main__':
    print('directamente desde la clase: {}'.format(E37Circulo.constant_pi()))

    CIRCULO1 = E37Circulo(4)
    print(CIRCULO1.area())
    print(CIRCULO1.constant_pi())

    CIRCULO2 = E37Circulo(4)
    print(CIRCULO2.area())
    print(CIRCULO2.constant_pi())
