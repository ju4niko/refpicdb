#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open("CheckPerms.py").read())
if AccesoSes(usuario,clave):
    print ("<h3>EDICION DE MAPA</h3>")
 
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

        print('<form method="post" action="inserta_mapa_commit.py">')
        print(f'<h4>{mapa}</h4>')
        print('<table>')

        print('<tr>')
        print('<td style="padding: 5px;">Objeto:</td>')
        print('<td style="padding: 5px;"><input list="objeto" name="objeto"><datalist id="objeto">')
        q = 'select t_name, t_id from tipos order by t_name asc'
        tot = cursor.execute(q)
        r = cursor.fetchall()
        for f in range(tot):
            print(f'<option value="{r[f][0]}:{r[f][1]}">')
        print('</datalist></td>')
        print('</tr>')

        print('<tr>')
        print('<td style="padding: 5px;">Bando:</td>')
        print('<td style="padding: 5px;"><input list="bando" name="bando"><datalist id="bando">')
        q = 'select b_name, b_id from bandos order by b_name asc'
        t1 = cursor.execute(q)
        r = cursor.fetchall()
        for g in range(t1):
            print(f'<option value="{r[g][0]}:{r[g][1]}">')
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

        print('</table>')

        print('<input type="submit" value="CREAR!">')
        print(f'<input type="hidden" id="map_id" name="map_id" value="{map_id}">')
        print(userpas)
        print('</form>')


    print ('<form method="post" action="menu_mapas.py">') # <--- poner aqui donde volver
    print (userpas)
    print ('<input type="submit" value=" <<< VOLVER" >')
    print ("</form>")
    
else:		
	print (GetOutOfHere)

print  ("</h4></center></body></html>")
cursor.close()
dbb.close()