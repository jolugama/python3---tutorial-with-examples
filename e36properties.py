#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=0n1GSt8ZFJ8&index=35&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E36usuario():
    '''properties:  acceso y modificacion de variables "privadas"(no lo son) con decoradores
    algo así como los getter y setter de java '''

    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password)
        self.email = email

    def __generar_password(self, password):
        return password.upper()+'xx' #menuda seguridad no? XD (lo pasa a mayusculas)


    @property
    def password(self):
        '''método getter para poder obtener el valor de una variable con name mangling '''
        return self.__password


    @password.setter
    def password(self, valor):
        self.__password = self.__generar_password(valor)




if __name__ == '__main__':
    USUARIO1 = E36usuario('jose', 'esto es un password', 'joseluis@jolugama.com')
    print(USUARIO1.password)
    USUARIO1.password = 'esto es otro password, modificado'
    print(USUARIO1.password)
    USUARIO1.password = 'esto es otro password, modificado2'
    print(USUARIO1.password)
