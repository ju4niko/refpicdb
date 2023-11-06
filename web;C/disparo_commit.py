#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open("CheckPerms.py").read())
import math


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

##################### MAIN ######################




if AccesoSes(usuario,clave):

    mapas = form.getvalue('mapas')
    b = form.getvalue("bando")
    w = form.getvalue("weapon")
    a = form.getvalue("ammo")
    p1 = str(form.getvalue('latlon'))
    elev = int(form.getvalue('elevacion'))
    azimut = int(form.getvalue('azimut'))


    print (elev,azimut)

    m_id = mapas.split(":")[1]

    bando = b.split(":")[0]
    b_id = b.split(":")[1]

    weapon = w.split(":")[0] 
    w_id = w.split(":")[1]

    ammo = a.split(":")[0] 
    a_id = a.split(":")[1]

    latlon = p1.split(",")
    lat = latlon[0]
    lon = latlon[1]

    cursor.execute(f'select a_vi from ammo where a_id = {a_id}')
    Vi = int((cursor.fetchone())[0])

    print (Vi)
    distancia = ((Vi ** 2 * math.sin( 2 * (elev/1000) )) / 9.81)
    lati, loni = calc_impacto(float(lat),float(lon), azimut, distancia)

    cursor.execute(f'insert into disparo \
        (d_lato,d_lono,d_latd,d_lond,m_id,b_id,w_id,a_id,d_dist) \
        values \
        ({lat},{lon},{lati},{loni},{m_id},{b_id},{w_id},{a_id},{int(distancia)})')
    dbb.commit()

    html = f"""
        <form id="redirectForm" method="post" action="ver_map.py">
            <input type="hidden" name="mapas" value="{mapas}">
            {userpas}
        </form>
        <script>
            window.onload = function() {{
                document.getElementById('redirectForm').submit();
            }};
        </script>
    """
    print(html)
else:	
	print ("USUARIO O CLAVE INCORRECTOS<br>")
	print ("---> ACCESO DENEGADO <---")
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" />')
	print ("</form><br>")	
print  ("</h4></center></body></html>")
cursor.close()
dbb.close() 
