#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=0n1GSt8ZFJ8&index=35&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E35Circulo():
    '''clase círculo. variables de clase'''
    _pi = 3.14159
    ''' pi pertenece a la clase, y puede ser accedida sin crear objetos.
    si se modifica pi, se modifica en todos los objetos'''
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        '''calcula area de un círculo'''
        return self.radio * self.radio * self._pi



if __name__ == '__main__':
    print('directamente desde la clase: {}'.format(E35Circulo._pi))

    CIRCULO1 = E35Circulo(4)
    print(CIRCULO1.area())
    print(CIRCULO1._pi)

    CIRCULO2 = E35Circulo(4)
    print(CIRCULO2.area())
    print(CIRCULO2._pi)
