#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Alejandra Reyes

import datetime
from datetime import date
from cuenta import Cuenta


def es_fecha(fec):
    if fec[-3] == '/' and fec[-6] == '/':
        anio = fec[6:8]
        mes = fec[3:5]
        dia = fec[0:2]
        try:
            dia = int(dia)
            if dia <= 31:
                mes = int(mes)
                if mes <= 12:
                    anio = int(anio)
                    return True
        except:
            return False

    return False

def dame_fecha():
    sw = False
    while not sw:
        dato = input('Dame la fecha de hoy dd/mm/aa')
        sw = es_fecha(dato)
    return dato

print(f'La fecha es {dame_fecha()}')



class Persona(object):
    def __init__(self, dni, nombre, str_fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = convertir_fecha(str_fecha_nacimiento)
        self.dni = dni
        self.cuentas = []

    def __str__(self):
        return f'Nombre: {self.nombre}'

    @property
    def edad(self):
        hoy = datetime.date.today()
        delta = hoy - self.fecha_nacimiento
        return int(delta.days/365)

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def crear_cuenta(self):
        # TODO: Segun la edad, debería crear Cuenta o CuentaJoven()
        cuenta = Cuenta()
        self.cuentas.append(cuenta)

    def obtener_todos_los_movimientos(self):
        todos_los_movimientos = []
        for cuenta in self.cuentas:
            todos_los_movimientos += cuenta.movimientos
        return todos_los_movimientos

    def saludo(self):
        # TODO: Saludo que indique hora fecha y clima
        return f"Persona saludando {self.nombre}"
