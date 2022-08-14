#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Alejandra Reyes

import pandas as pd
import numpy
import os
import csv
from persona import Persona


def crear_cuentas():
    """
    param: None
    :return: Lista de diccionarios
    """
    lista_de_tuplas = [('nro_de_cuenta', 'titular', 'saldo', 'activa')]
    for elemento in cuentas:
        lista_de_tuplas.append(tuple(elemento.values()))

    personas = {}
    archivo = open("personas.csv",  "w", newline='')
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerows
    titulos = next(archivo_csv)
    for nombre, dni, fecha_nacimiento in archivo_csv:
        persona = Persona(dni, nombre, fecha_nacimiento)
        persona.crear_cuenta()
        # La parte mas importante donde agrego al diccionario
        # con clave = dni el objecto persona
        personas[dni] = persona
    archivo.close()
    return personas


def procesar_gastos(cuentas, archivo):
    # TODO: procesar linea a linea del archivo, y aplicar a cada cuenta de las personas
    # Return: debe devolver las cuentas actualizadas
    archivo = open("gastos.csv")
    primer_linea = True
    for linea in archivo:
        if not primer_linea:
            # Aca proceso la linea
            nro_cuenta, importe_gasto = linea.replace('\n', '').split(',')  # En Win es '\r\n'
            importe_gasto_int = float(importe_gasto)
            cuentas_actualizadas = aplicar_gastos(cuentas, nro_cuenta, importe_gasto_int)
        else:
            primer_linea = False
    archivo.close()
    return cuentas_actualizadas



def procesar_depositos(cuentas, archivo):
    #     # TODO: procesar linea a linea del archivo, y aplicar a cada cuenta de las personas
    return: debe devolver las cuentas actualizadas



def procesar_transferencias(cuentas, archivo):
    # TODO: procesar linea a linea del archivo, y aplicar a cada cuenta de las personas
    return: debe devolver las cuentas actualizadas

