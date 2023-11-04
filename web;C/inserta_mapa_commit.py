#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave):

    map_id = form.getvalue('map_id')
    o = form.getvalue("objeto")
    b = form.getvalue("bando")

    bando = b.split(":")[0]
    b_id = b.split(":")[1]
 
    t_id = o.split(":")[1]
    objeto = o.split(":")[0]
    
    p1 = form.getvalue('latlon')
    latlon = p1.split(",")

    q = f'insert into objetos (t_id,o_lat,o_lng,b_id,m_id) values ({t_id},{latlon[0]},{latlon[1]},{b_id},{map_id})'
    
    cursor.execute(q)
    dbb.commit()
    print ("<center>OBJETO CREADO CORRECTAMENTE")
    print ('<form method="post" >')
    print (userpas)
    #print ('<button type="submit"  formaction="edit_map.py"> CREAR NUEVO</button>')
    print ('<button type="submit"  formaction="menu_mapas.py"> VOLVER </button>')
    print ("</form></center>")

else:	
	print ("USUARIO O CLAVE INCORRECTOS<br>")
	print ("---> ACCESO DENEGADO <---")
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" />')
	print ("</form><br>")	
print  ("</h4></center></body></html>")
cursor.close()
dbb.close()