#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgitb, cgi, datetime, sys, re
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import BaseDocTemplate, SimpleDocTemplate, Paragraph, Table, Frame, PageTemplate,TableStyle, PageBreak
from html import escape
from reportlab.lib.units import inch
from reportlab.lib.units import cm


import random
import math

cgitb.enable(display=0, logdir='./log')

SYS_NAME='NUMEROL SERVER'
VERSION='1.1'
DEF_BKGD="#EFEFEF"

form = cgi.FieldStorage()

angulo = float(form.getvalue("elevacion"))
direccion = int(form.getvalue("azimut"))
N = int(form.getvalue("salva"))
dispersion = int(form.getvalue("dispersion")    )
mortero = form.getvalue('mortero')
latitud_inicial = float(form.getvalue('latitud')   )
longitud_inicial = float(form.getvalue('longitud')    )

# Datos de coordenadas tres puntos de interes
punto1 = form.getvalue("punto1")
lat1 = float(form.getvalue('lat1'))
lng1 = float(form.getvalue('lng1'))
punto2 = form.getvalue("punto2")
lat2 = float(form.getvalue('lat2'))
lng2 = float(form.getvalue('lng2'))
punto3 = form.getvalue("punto3")
lat3 = float(form.getvalue('lat3'))
lng3 = float(form.getvalue('lng3'))

def generar_codigo_html(coordenadas, api_key):

    latitudes = [coord[0] for coord in coordenadas]
    longitudes = [coord[1] for coord in coordenadas]
    X = (coordenadas[0][0] + coordenadas[numCoordenadas - 1][0]) / 2;
    Y = (coordenadas[0][1] + coordenadas[numCoordenadas - 1][1]) / 2;

    latitud_media = (max(latitudes) + min(latitudes)) / 2
    longitud_media = (max(longitudes) + min(longitudes)) / 2

    #print("<!DOCTYPE html>")
    print('Content-Type:text/html;charset=utf-8\r\n')
    print('\r\n')
    print("<html>")
    print("  <head>")
    print(f"    <title>Mapa con Coordenadas</title>")
    print(f'    <script src="https://maps.googleapis.com/maps/api/js?key={api_key}"></script>')
    print("  </head>")
    print("  <body>")
    print('    <div id="map" style="height: 800px; width: 100%;"></div>')
    print("    <script>")
    print("      function initMap() {")
    print(f'        var map = new google.maps.Map(document.getElementById("map"), {{')
    print("          zoom: 18,")
    print(f'          center: {{ lat: {latitud_media:.6f}, lng: {longitud_media:.6f} }},')
    print("          mapTypeId: google.maps.MapTypeId.SATELLITE")
    print("        });")
	#Recorrer las coordenadas y agregar marcadores
    for i, (lat, lng) in enumerate(coordenadas):
        print(f'        new google.maps.Marker({{')
        print(f'          position: {{ lat: {lat:.6f}, lng: {lng:.6f} }},')
        print("          map: map,")
        if i == 0:
            print('          label: "Mtr"')
        elif i == len(coordenadas) - 1:
            print('          label: "Obj"')
        else:
            print(f'          label: "{i}"')
        print("        });")

        # Agregar el círculo centrado en las mismas coordenadas
        if i != 0 and i != len(coordenadas)-1:
          print(f'        new google.maps.Circle({{')
          print(f'          strokeColor: "#FF0000",')
          print('          strokeOpacity: 0.8,')
          print('          strokeWeight: 2,')
          print('          fillColor: "#600000",')
          print('          fillOpacity: 0.35,')
          print(f'          map: map,')
          print(f'          center: {{ lat: {lat:.6f}, lng: {lng:.6f} }},')
          print(f'          radius: {ammoDR}')  # Radio de mortalidad en metros
          print('        });')

	#agrego puntos de interes

    print(f'        new google.maps.Circle({{')
    print(f'          strokeColor: "#7000FF",')
    print('          strokeOpacity: 0.8,')
    print('          strokeWeight: 2,')
    print('          fillColor: "#700070",')
    print('          fillOpacity: 0.35,')
    print(f'          map: map,')
    print(f'          center: {{ lat: {lat1:.6f}, lng: {lng1:.6f} }},')
    print(f'          radius: 5')
    print('        });')
    print(f'        new google.maps.Circle({{')
    print(f'          strokeColor: "#7000FF",')
    print('          strokeOpacity: 0.8,')
    print('          strokeWeight: 2,')
    print('          fillColor: "#700070",')
    print('          fillOpacity: 0.35,')
    print(f'          map: map,')
    print(f'          center: {{ lat: {lat2:.6f}, lng: {lng2:.6f} }},')
    print(f'          radius: 5')
    print('        });')
    print(f'        new google.maps.Circle({{')
    print(f'          strokeColor: "#7000FF",')
    print('          strokeOpacity: 0.8,')
    print('          strokeWeight: 2,')
    print('          fillColor: "#700070",')
    print('          fillOpacity: 0.35,')
    print(f'          map: map,')
    print(f'          center: {{ lat: {lat3:.6f}, lng: {lng3:.6f} }},')
    print(f'          radius: 5')
    print('        });')

        # Agregar una etiqueta de texto cerca del círculo
    print(f'        var centerLatLng = new google.maps.LatLng({lat1:.6f}, {lng1:.6f});')
    print("        var textoEnCentro = new google.maps.InfoWindow({")
    print(f'          content: "{punto1}",')
    print("        });");
    print("        textoEnCentro.setPosition(centerLatLng);")
    print("        textoEnCentro.open(map);")

    print(f'        var centerLatLng = new google.maps.LatLng({lat2:.6f}, {lng2:.6f});')
    print("        var textoEnCentro = new google.maps.InfoWindow({")
    print(f'          content: "{punto2}",')
    print("        });");
    print("        textoEnCentro.setPosition(centerLatLng);")
    print("        textoEnCentro.open(map);")

    print(f'        var centerLatLng = new google.maps.LatLng({lat3:.6f}, {lng3:.6f});')
    print("        var textoEnCentro = new google.maps.InfoWindow({")
    print(f'          content: "{punto3}",')
    print("        });");
    print("        textoEnCentro.setPosition(centerLatLng);")
    print("        textoEnCentro.open(map);")


	#Agregar una línea con forma de flecha entre el primer y último punto con texto en el centro
    print("        var flightPath = new google.maps.Polyline({")
    print("          path: [")
    #for lat, lng in coordenadas:
    print(f'            {{ lat: {coordenadas[0][0]:.6f}, lng: {coordenadas[0][1]:.6f} }},')
    print(f'            {{ lat: {coordenadas[numCoordenadas - 1][0]:.6f}, lng: {coordenadas[numCoordenadas - 1][1]:.6f} }}')
    print("          ],")
    print("          geodesic: true,")
    print("          icons: [{")
    print('            icon: { path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW },')
    print("            offset: '100%',")
    print("          }],")
    print("          strokeColor: '#FFFF00',")
    print("          strokeOpacity: 1.0,")
    print("          strokeWeight: 5")
    print("        });")
    print("        flightPath.setMap(map);")

    #Crear un texto en el centro de la línea
    print(f'        var centerLatLng = new google.maps.LatLng({X:.6f}, {Y:.6f});')
    print("        var textoEnCentro = new google.maps.InfoWindow({")
    print(f'          content: "{distancia:.2f} m, {ammoType}",')
    print("        });");
    print("        textoEnCentro.setPosition(centerLatLng);")
    print("        textoEnCentro.open(map);")







    print("      }")
    print("    </script>")
    print("    <script>")
    print("      initMap();")
    print("    </script>")
    print("  </body>")
    print("</html>")

def add_wobble(valor_inicial, porcentaje_maximo):
    # Generar un número aleatorio entre -1 y 1
    signo_aleatorio = (random.random() * 2) - 1

    # Calcular el valor aleatorio dentro del rango
    valor_aleatorio = signo_aleatorio * porcentaje_maximo * valor_inicial

    # Calcular el valor final
    valor_final = valor_inicial + valor_aleatorio

    return valor_final

def calcular_distancia_proyectil(angulo, velocidad_inicial):
    gravedad = 9.81

    # Convertir el ángulo de grados a radianes
    angulo_radianes = math.radians(angulo)

    # Calcular la distancia
    distancia = (velocidad_inicial ** 2 * math.sin(2 * angulo_radianes)) / gravedad

    return distancia

def calcular_coordenadas_impacto(latitud_inicial, longitud_inicial, direccion, distancia):
    radio_tierra = 6371000

    # Convertir la dirección en grados a radianes
    direccion_radianes = math.radians(direccion)

    # Convertir latitud y longitud inicial a radianes
    latitud_radianes = math.radians(latitud_inicial)
    longitud_radianes = math.radians(longitud_inicial)

    # Calcular las coordenadas cartesianas del impacto
    x_impacto = distancia * math.cos(direccion_radianes)
    y_impacto = distancia * math.sin(direccion_radianes)

    # Calcular las coordenadas esféricas del impacto
    nueva_latitud_radianes = math.asin(math.sin(latitud_radianes) * math.cos(distancia / radio_tierra) + math.cos(latitud_radianes) * math.sin(distancia / radio_tierra) * math.cos(direccion_radianes))
    nueva_longitud_radianes = longitud_radianes + math.atan2(math.sin(direccion_radianes) * math.sin(distancia / radio_tierra) * math.cos(latitud_radianes), math.cos(distancia / radio_tierra) - math.sin(latitud_radianes) * math.sin(nueva_latitud_radianes))

    # Convertir las coordenadas esféricas del impacto a grados
    latitud_impacto = math.degrees(nueva_latitud_radianes)
    longitud_impacto = math.degrees(nueva_longitud_radianes)

    return latitud_impacto, longitud_impacto

##################### MAIN ######################


#caracteristicas de la municion, velocidad inicial y radio de letalidad
ammoVi = 44
ammoDR = 5
ammoType = 'HE-60mm'

distancia = calcular_distancia_proyectil(angulo, ammoVi)

latitud_impacto, longitud_impacto = calcular_coordenadas_impacto(latitud_inicial, longitud_inicial, direccion, distancia)

coordenadas = [(latitud_inicial, longitud_inicial)]
for _ in range(N):
    latitud = add_wobble(latitud_impacto, dispersion / 10000000)
    longitud = add_wobble(longitud_impacto, dispersion / 10000000)
    coordenadas.append((latitud, longitud))

coordenadas.append((latitud_impacto, longitud_impacto))

numCoordenadas = len(coordenadas)

api_key = "AIzaSyA5FuC-FpZNRVKEl2ZxzEm4DLoC9Mkgg3Y"



generar_codigo_html(coordenadas, api_key)

