#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave):

    print ("<h3> MENU DISPARO </h3>")
    
    mapas = form.getvalue('mapas')
    mapa = mapas.split(":")[0]
    map_id = mapas.split(":")[1]
    
    q = f'select m_id from mapas where m_nom = "{mapa}"'
    cursor.execute(q)
    r = cursor.fetchone()
    dbb.commit()
    if r == None:
        print(f'MAPA INEXISTNTE!')
    else:        

        print('<form method="post" action="disapro_commit.py">')
        print(f'<h4>MAPA:{mapa}</h4>')

        print('<table>')

        print('<tr>')
        print('<td style="padding: 5px;">Bando:</td>')
        print('<td style="padding: 5px;"><input list="bando" name="bando"><datalist id="bando">')
        cursor.execute('select b_name, b_id from bandos order by b_name asc')
        for b_name, b_id in cursor.fetchall(): print(f'<option value="{b_name}:{b_id}">')
        print('</datalist></td>')
        print('</tr>')

        print('<tr>')
        print('<td style="padding: 5px;">Armamento:</td>')
        print('<td style="padding: 5px;"><input list="weapon" name="weapon"><datalist id="weapon">')
        cursor.execute('select w_name, w_id from weapon')
        for w_name,w_id in cursor.fetchall(): print(f'<option value="{w_name}:{w_id}">')
        print('</datalist></td>')
        print('</tr>')

        print('<tr>')
        print('<td style="padding: 5px;">Municion:</td>')
        print('<td style="padding: 5px;"><input list="ammo" name="ammo"><datalist id="ammo">')
        cursor.execute('select a_name, a_id, a_vi from ammo')
        for a_name,a_id,a_vi in cursor.fetchall():
            print(f'<option value="{a_name}:{a_id}">')
        print('</datalist></td>')
        print('</tr>')

        print('<tr>')
        print('<td style="padding: 5px;">Lat,Lon:</td>')
        print('<td style="padding: 5px;"><input \
            type="text" \
            name="latlon" \
            id="latlon" \
            value="" \
            maxlength="40" \
            autocomplete="off" \
            size="25"\
            title="Formato +/-LAT.decimales, +/-LON.decimales ej: -34.123456, -58.123456."\
            ></td>')
        print('</tr>')

        print('<tr>')
        print('<td style="padding: 5px;">Elevacion (mils):</td>')
        print('<td style="padding: 5px;"><input \
            type="text" \
            name="latlon" \
            id="latlon" \
            value="" \
            maxlength="20" \
            autocomplete="off" \
            size="25"\
            title="angulo de elevacion en miliradianes"\
            ></td>')
        print('</tr>')
 
        print('<tr>')
        print('<td style="padding: 5px;">Azimut (mils):</td>')
        print('<td style="padding: 5px;"><input \
            type="text" \
            name="azimut" \
            id="azimut" \
            value="" \
            maxlength="40" \
            autocomplete="off" \
            size="25"\
            title="angulo de azimut en miliradianes"\
            ></td>')
        print('</tr>')
 
        print('</table>')

        
        print('<input type="submit" value="FUEGO!">')
        print(f'<input type="hidden" id="map_id" name="map_id" value="{map_id}">')
        print(userpas)
        print('</form>')

        print ('<h3>TABLAS DE TRAYECTORIAS --->')
        print ('<form method="post" action="tablas_trayectorias.py">')
        print ('<input type="submit" value="VER" /></h3>')
        print (userpas)
        print('</form>')


        print ('<br><br><form method="post" action="menu_mapas.py">') # <--- opner aqui donde volver
        print ('<input type="submit" value=" <<< VOLVER" >')
        print (userpas)
        print ("</form>")  
else:	
	print ("USUARIO O CLAVE INCORRECTOS<br>")
	print ("---> ACCESO DENEGADO <---")
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" />')
	print ("</form><br>")	
print  ("</h4></center></body></html>")
cursor.close()
dbb.close()    