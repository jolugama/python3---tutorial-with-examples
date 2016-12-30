#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=_4QUMUlI2S8&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM&index=24
codigo facilito
'''

from e23docstring import E23  # importamos la clase del ejercicio anterior


class E24():
    ''' modulos
    cuando tenemos un proyecto grande, hay que modularizar el proyecto
    Separar el código
    '''

    def __init__(self):
        ejercicio_anterior = E23 #asignamos una variable a la clase importada
        ejercicio_anterior().funcion1() #llamamos a la funcion1 de la clase importada
        temp = ejercicio_anterior().funcion2(4, 3) #llamamos a la funcion2 de la clase importada
        print(temp)


#ejecuto la clase
E24()


'''
Comprobar que se ha creado una carpeta __pycache__ y dentro un archivo
empezando por la clase del ejercicio anterior, con extensión pic

Eso hace que cuando se vuelva a ejecutar, python lo haga más rápido
'''
