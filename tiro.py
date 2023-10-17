#!/usr/bin/python3
import random
import math

def generar_codigo_html(coordenadas, api_key):
    latitudes = [coord[0] for coord in coordenadas]
    longitudes = [coord[1] for coord in coordenadas]

    latitud_media = (max(latitudes) + min(latitudes)) / 2
    longitud_media = (max(longitudes) + min(longitudes)) / 2

    print("<!DOCTYPE html>")
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

    print("        var flightPath = new google.maps.Polyline({")
    print("          path: [")
    for lat, lng in coordenadas:
        print(f'            {{ lat: {lat:.6f}, lng: {lng:.6f} }},')
    print("          ],")
    print("          geodesic: true,")
    print("          icons: [{")
    print('            icon: { path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW },')
    print("            offset: '100%',")
    print("          }],")
    print("          strokeColor: '#FF0000',")
    print("          strokeOpacity: 1.0,")
    print("          strokeWeight: 2")
    print("        });")

    print("        flightPath.setMap(map);")
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

def main():
    if len(sys.argv) != 7:
        print("Uso: {} <Lat> <Long> <disparos> <azimut> <direccion> <dispersion>".format(sys.argv[0]))
        return 1

    latitud_inicial = float(sys.argv[1])
    longitud_inicial = float(sys.argv[2])
    N = int(sys.argv[3])
    angulo = float(sys.argv[4])
    direccion = float(sys.argv[5])
    dispersion = float(sys.argv[6])

    distancia = calcular_distancia_proyectil(angulo, 90)
    latitud_impacto, longitud_impacto = calcular_coordenadas_impacto(latitud_inicial, longitud_inicial, direccion, distancia)

    coordenadas = [(latitud_inicial, longitud_inicial)]
    for _ in range(N):
        latitud = add_wobble(latitud_impacto, dispersion / 10000000)
        longitud = add_wobble(longitud_impacto, dispersion / 10000000)
        coordenadas.append((latitud, longitud))

    coordenadas.append((latitud_impacto, longitud_impacto))

    api_key = "AIzaSyA5FuC-FpZNRVKEl2ZxzEm4DLoC9Mkgg3Y"

    generar_codigo_html(coordenadas, api_key)

if __name__ == "__main__":
    import sys
    main()
