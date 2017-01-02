#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
https://www.youtube.com/watch?v=44D-QCg-YEw&t=13s&list=PLpOqH6AE0tNiK7QN6AJo_3nVGQPc8nLdM&index=28
https://www.youtube.com/watch?v=g1lpoJkPQiM  fechas
codigo facilito
'''


import random
from datetime import date, datetime, timedelta
import sys
import time


class E28():
    ''' modulos
    Python viene con baterías incluidas
    Hay muchas liberías útiles que nos permiten ahorrarnos el tiempo de crearlos nosotros

    3 librerías: random, datetime
    '''

    def __init__(self):
        '''
        ******** librería random ********
        '''
        # random
        # asigno a valor un número aleatorio entre 0 y 10
        valor = random.randint(0, 10)
        lista = [True, "strings", 23, 1.98]
        valor2 = random.choice(lista)  # elijo un valor de la lista aleatorio

        print(valor)
        print(valor2)

        print(lista)
        random.shuffle(lista)  # desordena la lista
        print(lista)


        '''
        ******** librería datetime (date, datetime, timedelta) ********
        '''
        # date
        print(date.today())
        print('El día actual es {}'.format(date.today().day))
        print('El mes actual es {}'.format(date.today().month))
        print('El año actual es {}'.format(date.today().year))

        # datetime : tiene a parte de la fecha, las horas, minutos, segundos.
        print(datetime.now())
        print('la hora actual es {}'.format(datetime.now().hour))
        print('El minuto actual es {}'.format(datetime.now().minute))
        print('El segundo actual es {}'.format(datetime.now().second))

        # creación de una fecha
        # se puede añadir hora, minutos, segundos, y milisegundos
        new_date = datetime(2016, 12, 30)
        print('la nueva fecha es {}'.format(new_date))
        print(type(new_date))

        # comparación, modificacion de fechas
        # suma 10 días de la fecha anterior
        new_date2 = new_date + timedelta(days=10)
        print(new_date2)

        # formato de fechas
        # dia, mes en letras (en ingles), año
        print(new_date2.strftime('%d, %b, %Y'))

        # en castellano
        def fecha_actual(fecha):
            '''workarround que nos muestra el formato de fecha en español,
            de la forma que queramos'''
            months = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                      'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
            return "{d} de {m} del {y}".format(d=fecha.day, m=months[fecha.month - 1], y=fecha.year)

        print(fecha_actual(datetime.now()))


        '''
        ******** librería sys ********
        el encargado de proveer variables y funcionalidades,
         directamente relacionadas con el intérprete.
        '''
        for i in range(101):
            time.sleep(0.05)
            sys.stdout.write('\r%d %%' %i)
            sys.stdout.flush()

        print('finalizado!!')


if __name__ == '__main__':
    E28()
