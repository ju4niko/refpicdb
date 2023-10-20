#!/usr/bin/python3
# -*- coding: utf-8 -*-

with open("inicio.html", 'r') as archivo:
    print('Content-Type:text/html;charset=utf-8')
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea, end='')
