#!/usr/bin/env python3
import sys
import numpy as np
import matplotlib.pyplot as plt

def calcular_trayectoria(Vi, angulo_miliradianes):
    angulo_radianes = angulo_miliradianes / 1000.0
    g = 9.81
    tiempo_vuelo = (2 * Vi * np.sin(angulo_radianes)) / g
    t = np.linspace(0, tiempo_vuelo, num=1000)
    x = Vi * np.cos(angulo_radianes) * t
    y = Vi * np.sin(angulo_radianes) * t - (0.5 * g * t**2)
    return x, y, tiempo_vuelo

def dibujar_intervalo_trayectorias(Vi, angulo_inicial_miliradianes, incremento_miliradianes, num_trayectorias):
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.xlabel('Alcance (metros)')
    plt.ylabel('Altura (metros)')
    plt.title(f'Municion Vi={Vi} m/s')
    plt.grid(True)
    max_x = 0
    min_x = 100000000
    for i in range(num_trayectorias):
        angulo_actual = angulo_inicial_miliradianes + i * incremento_miliradianes
        x, y, _ = calcular_trayectoria(Vi, angulo_actual)
        etiqueta = f'{int(angulo_actual)} mils'
        plt.plot(x, y, label=etiqueta)
        max_x = max(max_x, max(x))  # Actualizar el valor máximo de x
        min_x = min(min_x,min(max(x),100000000))
        
    plt.legend()
    interv =100

    if max_x < 1000: interv = 50
    if max_x < 500: interv = 25
    if max_x < 400: interv = 20
    if max_x < 200: interv = 10

    #xticks = np.arange(0, max_x, interv )
    #ax.set_xticks(xticks)
    # Marcar el valor máximo en el eje X con una etiqueta
    ax.axvline(max_x, color='b', linestyle='--')  # Línea vertical
    ax.axvline(min_x, color='r', linestyle='--')  # Línea vertical
    ax.annotate(f'{int(max_x)}', xy=(max_x, 0), xytext=(10, 3),textcoords='offset points', color='b', ha='center')
    ax.annotate(f'{int(min_x)}', xy=(min_x, 0), xytext=(10, 3),textcoords='offset points', color='r', ha='center')
    
    plt.show()

if len(sys.argv) != 5:
    print("Uso: python script.py <Vi (m/s)> <Elevacion (mils)> <Incremento (mils)> <Repeticiones>")
    sys.exit(1)

try:
    Vi = float(sys.argv[1])
    angulo_inicial_miliradianes = float(sys.argv[2])
    incremento_miliradianes = float(sys.argv[3])
    num_trayectorias = int(sys.argv[4])
except ValueError:
    print("Error: Ingresa valores numéricos válidos para Velocidad Inicial, Ángulo Inicial, Incremento y Cantidad de Trayectorias.")
    sys.exit(1)

dibujar_intervalo_trayectorias(Vi, angulo_inicial_miliradianes, incremento_miliradianes, num_trayectorias)
