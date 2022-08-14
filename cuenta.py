#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Alejandra Reyes

import datetime


class Cuenta(object):

    def __init__(self, monto_inicio=0, numero_de_cuenta=0):  # contructor, siempre de la misma forma
        self.cantidad = monto_inicio
        self.numero_de_cuenta = numero_de_cuenta
        self.movimientos = []
        self.activa = True

    def aplicar_gasto(self, monto):  # retirar
        self.__cantidad = self.__cantidad - monto
        print(f"Monto retirado:\t\t {monto}\n" \
              f"Saldo cuenta:\t\t {self.__cantidad}")


    def aplicar_deposito(self, monto):  # ingresar
        if monto >= 0:
            self.__cantidad = self.__cantidad + monto
            print(f"Monto ingresado:\t {monto}\n" \
                  f"Saldo cuenta:\t\t {self.__cantidad}")

    def desactivar(self):
        # TODO: Solo si el saldo es cero
        self.activa = False

    def activar(self):
        # TODO: Solo si el saldo es cero
        self.activa = True

    def crear_movimiento(self, descripcion, monto):
        movimiento = MovimientoCuenta(descripcion, monto)
        self.movimientos.append(movimiento)

    def __str__(self):
        # TODO: Completar para que quede mejor con nro de cuenta
        print(f"CUENTA comun {self.cantidad}")


class CuentaJoven(Cuenta):

    def __init__(self, bonificacion, monto_inicio=0, numero_de_cuenta=0):
        Cuenta.__init__(self, monto_inicio, numero_de_cuenta)
        self.bonificacion = bonificacion

    def __str__(self):
        return f'CuentaJoven({self.bonificacion}
        # TODO: Completar para que quede mejor
        print(f"CUENTA JOVEN {self.cantidad}")

@property
    def bonificacion(self):
        print(f"Bonificacion: {self.__bonificacion}")


@property
def bonificacion(self):
    return self.__bonificacion


@bonificacion.setter
def bonificacion(self, bonificacion):
    self.__bonificacion = bonificacion


def mostrar(self):
    return "Cuenta Joven\n" + "Titular:" + self.titular.mostrar() + " - Cantidad:" + str(
        self.cantidad) + "- Bonificación:" + str(self.bonificacion) + "%"


def esTitularValido(self):
    return self.titular.edad < 18 and self.titular.esMayorDeEdad()


def retirar(self, cantidad):
    if not self.esTitularValido():
        print("No puesdes retirar el dinero. titular no válido")
    elif cantidad > 0:
        super().retirar(cantidad)


cuentaJ = cuentaJoven("")
cuentaJ.bonificacion


class MovimientoCuenta(object):

    def __init__(self, descripcion, monto_del_movimiento):
        self.fecha_y_hora = datetime.datetime.now()
        self.descripcion = descripcion
        self.monto = monto_del_movimiento

    def __str__(self):
        # TODO: Completar como pide el ejercicio 3)
        return f"{self.fecha_y_hora} {self.descripcion} {self.monto}"
