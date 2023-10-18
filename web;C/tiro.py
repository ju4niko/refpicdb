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

BOMBAZO="#FF0000"
BOMBAZO_FILL="#8F0000"
POI_A="#FF00FF"
POI_A_FILL="#7F007F"
POI_B="#00FFFF"
POI_B_FILL="#6F6F00"
AMARILLO="#FFFF00"

################################################################################
################################################################################
class GoogleMapsHelper:
    def __init__(self):
        self.objects = []

    def add_circle(self, lat, lng, radius, stroke_color=BOMBAZO, fill_color=BOMBAZO_FILL, stroke_opacity=0.8, fill_opacity=0.35):
        circle = {
            "type": "circle",
            "lat": lat,
            "lng": lng,
            "radius": radius,
            "stroke_color": stroke_color,
            "fill_color": fill_color,
            "stroke_opacity": stroke_opacity,
            "fill_opacity": fill_opacity,
        }
        self.objects.append(circle)

    def add_text_label(self, lat, lng, content):
        text_label = {
            "type": "text_label",
            "lat": lat,
            "lng": lng,
            "content": content,
        }
        self.objects.append(text_label)

    def add_marker(self, lat, lng, valor):
        marker = {
            "type": "marker",
            "lat": lat,
            "lng": lng,
            "label": valor,
        }
        self.objects.append(marker)

    def add_line(self,x0,y0,x1,y1,color,grosor):
        linea = {
            "type": "linea",
            "x0": x0,
            "y0": y0,
            "x1": x1,
            "y1": y1,
            "stroke_color": color,
            "grosor": grosor,
        }
        self.objects.append(linea)

    def add_flecha(self,x0,y0,x1,y1,color=AMARILLO,grosor=5):
        linea = {
            "type": "linea",
            "x0": x0,
            "y0": y0,
            "x1": x1,
            "y1": y1,
            "stroke_color": color,
            "grosor": grosor,
        }
        self.objects.append(linea)

    def add_square(self, lat, lng, size, stroke_color=POI_A, fill_color=POI_B, stroke_opacity=0.8, fill_opacity=0.35):


        square = {
            "type": "square",
            "lat": lat,
            "lng": lng,
            "size": size/55560,
            "stroke_color": stroke_color,
            "fill_color": fill_color,
            "stroke_opacity": stroke_opacity,
            "fill_opacity": fill_opacity,
        }
        self.objects.append(square)


    def generate_js_code(self):
        js_code = []
        for obj in self.objects:
            if obj["type"] == "circle":
                js_code.append(f'new google.maps.Circle({{')
                js_code.append(f'  strokeColor: "{obj["stroke_color"]}",')
                js_code.append(f'  strokeOpacity: {obj["stroke_opacity"]},')
                js_code.append('  strokeWeight: 2,')
                js_code.append(f'  fillColor: "{obj["fill_color"]}",')
                js_code.append(f'  fillOpacity: {obj["fill_opacity"]},')
                js_code.append(f'  map: map,')
                js_code.append(f'  center: {{ lat: {obj["lat"]:.6f}, lng: {obj["lng"]:.6f} }},')
                js_code.append(f'  radius: {obj["radius"]}')
                js_code.append('});')
            elif obj["type"] == "text_label":
                js_code.append(f'var centerLatLng = new google.maps.LatLng({obj["lat"]:.6f}, {obj["lng"]:.6f});')
                js_code.append("var textoEnCentro = new google.maps.InfoWindow({")
                js_code.append(f'  content: "{obj["content"]}",')
                js_code.append("});")
                js_code.append("textoEnCentro.setPosition(centerLatLng);")
                js_code.append("textoEnCentro.open(map);")
            elif obj["type"] == "marker":
                js_code.append(f'new google.maps.Marker({{')
                js_code.append(f' position: {{ lat: {obj["lat"]:.6f}, lng: {obj["lng"]:.6f} }},')
                js_code.append(f'  map: map,')
                js_code.append(f'  label: "{obj["label"]}"')
                js_code.append('});')
            elif obj["type"] == "linea" or obj["type"] == "flecha":
                js_code.append("        var flightPath = new google.maps.Polyline({")
                js_code.append("          path: [")
                js_code.append(f'            {{ lat: {obj["x0"]:.6f}, lng: {obj["y0"]:.6f} }},')
                js_code.append(f'            {{ lat: {obj["x1"]:.6f}, lng: {obj["y1"]:.6f} }},')
                js_code.append("          ],")
                js_code.append("          geodesic: true,")
                if obj["type"] == "flecha":
                    js_code.append("          icons: [{")
                    js_code.append('            icon: { path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW },')
                    js_code.append("            offset: '100%',")
                    js_code.append("          }],")
                js_code.append(f'  strokeColor: "{obj["stroke_color"]}",')
                js_code.append(f'  strokeWeight: {obj["grosor"]},')
                js_code.append("        });")
                js_code.append("        flightPath.setMap(map);")
            elif obj["type"] == "square":
                half_size = obj["size"] / 2
                js_code.append(f'new google.maps.Rectangle({{')
                js_code.append(f'  strokeColor: "{obj["stroke_color"]}",')
                js_code.append(f'  strokeOpacity: {obj["stroke_opacity"]},')
                js_code.append(f'  fillColor: "{obj["fill_color"]}",')
                js_code.append(f'  fillOpacity: {obj["fill_opacity"]},')
                js_code.append(f'  map: map,')
                js_code.append(f'  bounds: {{')
                js_code.append(f'    north: {obj["lat"] + half_size:.6f},')
                js_code.append(f'    south: {obj["lat"] - half_size:.6f},')
                js_code.append(f'    east: {obj["lng"] + half_size:.6f},')
                js_code.append(f'    west: {obj["lng"] - half_size:.6f}')
                js_code.append('  }')
                js_code.append('});')

        return "\n".join(js_code)
################################################################################



cgitb.enable(display=0, logdir='./log')

SYS_NAME='TIRO SERVER'
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

################################################################################

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

    #creo objeto para agregar items al mapa
    gmaps = GoogleMapsHelper()

	#Recorrer las coordenadas y agregar marcadores
    for i, (lat, lng) in enumerate(coordenadas):

        if i == 0:
            gmaps.add_marker(lat,lng,"Mtr")
        elif i == len(coordenadas) - 1:
            gmaps.add_marker(lat,lng,"Obj")
        else:
            gmaps.add_marker(lat,lng,f'{i}')

        # Agregar el círculo centrado en las mismas coordenadas
        #se saltea el origen y destino
        if i != 0 and i != len(coordenadas)-1:
            gmaps.add_circle(lat,lng,ammoDR)

	#cuadrados en puntos de inrteres
    gmaps.add_square(lat1,lng1,5)
    gmaps.add_square(lat2,lng2,5)
    gmaps.add_square(lat3,lng3,5)

    # Agregar una etiqueta de texto cerca de los POI
    gmaps.add_text_label(lat1,lng1,punto1)
    gmaps.add_text_label(lat2,lng2,punto2)
    gmaps.add_text_label(lat3,lng3,punto3)

	#Agregar una línea con forma de flecha entre el primer y último punto con texto en el centro
    gmaps.add_flecha(coordenadas[0][0],coordenadas[0][1],coordenadas[numCoordenadas - 1][0],coordenadas[numCoordenadas - 1][1])

    #Crear un texto en el centro de la línea
    gmaps.add_text_label(X,Y,f'{distancia:.2f} m, {ammoType}')

    print(gmaps.generate_js_code())

	#cierre del HTML
    print("      }")
    print("    </script>")
    print("    <script>")
    print("      initMap();")
    print("    </script>")
    print("  </body>")
    print("</html>")

################################################################################

def add_wobble(valor_inicial, porcentaje_maximo):
    # Generar un número aleatorio entre -1 y 1
    signo_aleatorio = (random.random() * 2) - 1

    # Calcular el valor aleatorio dentro del rango
    valor_aleatorio = signo_aleatorio * porcentaje_maximo * valor_inicial

    # Calcular el valor final
    valor_final = valor_inicial + valor_aleatorio

    return valor_final
################################################################################

def calcular_distancia_proyectil(angulo, velocidad_inicial):
    gravedad = 9.81

    # Convertir el ángulo de grados a radianes
    angulo_radianes = math.radians(angulo)

    # Calcular la distancia
    distancia = (velocidad_inicial ** 2 * math.sin(2 * angulo_radianes)) / gravedad

    return distancia
################################################################################

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
################################################################################

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

