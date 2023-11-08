#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open("CheckPerms.py").read())
import CalculoBalistico as CB
import math
##################### MAIN ######################

if AccesoSes(usuario,clave):

    mapas = form.getvalue('mapas')
    b = form.getvalue("bando")
    w = form.getvalue("weapon")
    a = form.getvalue("ammo")
    p1 = str(form.getvalue('latlon'))
    elev = int(form.getvalue('elevacion'))
    azimut = int(form.getvalue('azimut'))

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

    cursor.execute(f'select a_vi,a_mil from ammo where a_id = {a_id}')
    r = cursor.fetchone()
    Vi = int(r[0])
    MIL = int(r[1])
    FACTOR_MIL = float(MIL/(2*3.14159*1000))

    distancia = ((Vi ** 2 * math.sin( 2 * ( (elev/FACTOR_MIL ) /1000) )) / 9.81)
    lati, loni = CB.calc_impacto(float(lat),float(lon), azimut/FACTOR_MIL, distancia)

    cursor.execute(f'insert into disparo \
        (d_lato,d_lono,d_latd,d_lond,m_id,b_id,w_id,a_id,d_dist) \
        values \
        ({lat},{lon},{lati},{loni},{m_id},{b_id},{w_id},{a_id},{int(distancia)})')
    dbb.commit()

    html = f"""
        <form id="redirectForm" method="post" action="ver_map.py">
            <input type="hidden" name="mapas" value="{mapas}">
            <input type="hidden" name="bando" value="{b}">
            <input type="hidden" name="verDisp" value="1">
            <input type="hidden" name="limite_disp" value="1">
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
