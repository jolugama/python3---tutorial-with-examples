#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=XTTwSkIPZIw&index=33&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E34():
    ''' métodos y atributos privados
    En realidad no existen en python. Siempre se pueden acceder,
    aunque si se puede dificultar el acceso de dos formas:
    *añadiendo un guion bajo al principio, aunque se accede sin problemas
    *mediante name mangling, con dos guiones bajos al principio,
     esta última dificulta algo el acceso, al menos no da a equívocos para
     el programador, aunque cualquiera puede acceder a ellos.'''

    def __init__(self):
        #variable 'privada', no hay dificultad en el acceso a ella desde fuera
        #solo avisa al programador de que se toma como privada
        self._variable_privada = 'hola, soy una variable privada'

        #variable 'privada' con name mangling, el acceso es un poco mas dificil
        self.__variable_con_name_mangling = 'soy más dificil de acceder'

    def _metodo_privado(self):
        print('metodo privado')

    def __metodo_con_name_mangling(self):
        print('metodo con name mangling')


if __name__ == '__main__':
    EJ34 = E34()
    #pylint, en todos los casos mostrará aviso de que no se debe acceder a miembros protegidos
    print(EJ34._variable_privada)
    print(EJ34._E34__variable_con_name_mangling)
    EJ34._metodo_privado()
    EJ34._E34__metodo_con_name_mangling()
    