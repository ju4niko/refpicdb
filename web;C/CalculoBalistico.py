import math
################################################################################
def add_wobble(valor_inicial, porcentaje_maximo):
    signo_aleatorio = (random.random() * 2) - 1
    valor_aleatorio = signo_aleatorio * porcentaje_maximo * valor_inicial
    return valor_inicial + valor_aleatorio

################################################################################
def calc_impacto(latitud_inicial, longitud_inicial, direccion, distancia):
    radio_tierra = 6371000
    # Convertir la dirección en miliradianes a radianes
    direccion_radianes = direccion/1000
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
