#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=XTTwSkIPZIw&index=33&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM
codigo facilito
'''


class E33coche():
    ''' init, el inicializador de clases de python
    ejemplo típico coche, que inicializamos mediante init los atributos
    y hacemos usos de sus métodos.
    cada clase se puede asignar a x objetos independientes que contarán
    con distintos estados diferentes según se usen sus métodos y atributos'''

    def __init__(self, marca, modelo, color):
        self.marca = marca or 'desconocida'
        self.modelo = modelo or 'desconocido'
        self.color = color or 'blanco'
        self.cuenta_kilometros = 0
        self.velocidad = 0
        self.pitidos = 0
        self.arrancado = False

    def _pre(self):
        '''funcion privada. imprime antes de todos los pring la marca, modelo y color'''
        return '[{} {} {}]:'.format(self.marca, self.modelo, self.color)

    def arrancar(self):
        ''' arranca el coche si no está arrancado'''
        if not self.arrancado:
            print(self._pre()+'ñec ñec ñec bruuuuuuuuuuuuum brumm brummm bruuuummmmmm. arrancado')
            self.arrancado = True
        else:
            # Dale al encendido estando el coche arrancado y escucha...
            print(self._pre()+'argggggggggg!!! ')

    def parar(self):
        ''' para el motor del coche '''
        if self.arrancado is True:
            self.arrancado = False
        else:
            print(self._pre()+'error, el coche ya estaba parado')

    def acelerar(self):
        '''aumenta de velocidad'''
        if self.arrancado:
            self.velocidad += 1
            self.cuenta_kilometros += 0.015
        else:
            print(self._pre()+'error, el coche no está arrancado')

    def frenar(self):
        '''disminuye de velocidad'''
        if self.velocidad > 0:
            self.velocidad = self.velocidad - 1
            self.cuenta_kilometros += 0.015
        else:
            print(self._pre()+'error. el coche ya se encuentra frenado')

    def pitar(self):
        '''presiona el claxon'''
        print(self._pre()+'piiiiii  piii piiiiiiiiiii')
        self.pitidos += 1
        if self.pitidos > 5:
            print(self._pre()+'eeei, demasiados pitidos!!!')

    def consultar_coche(self):
        '''consulta los datos introducidos del tipo de coche'''
        resul = 'marca: {}, modelo:{}, color:{}'.format(
            self.marca, self.modelo, self.color)
        print(self._pre()+resul)

    def consultar_velocimetro(self):
        '''consulta la velocidad actual'''
        print(self._pre()+'La velocidad es {}km/s'.format(self.velocidad))

    def consultar_cuenta_kilometros(self):
        '''consulta los kilómetros actuales'''
        print(self._pre()+'Los kilómetros actuales son {}km'.format(self.cuenta_kilometros))


if __name__ == '__main__':
    COCHE1 = E33coche('seat', 'leon', 'amarillo')
    COCHE1.consultar_coche()
    COCHE1.parar()
    COCHE1.arrancar()
    COCHE1.consultar_velocimetro()
    COCHE1.consultar_cuenta_kilometros()
    for i in range(100):
        COCHE1.acelerar()
    for i in range(102):
        COCHE1.frenar()
    COCHE1.consultar_velocimetro()
    COCHE1.consultar_cuenta_kilometros()
    for i in range(6):
        COCHE1.pitar()
   