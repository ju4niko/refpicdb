#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open("CheckPerms.py").read())

if AccesoSuAdmin(usuario):    
    mapa = form.getvalue('mapa')
    q = f'INSERT INTO mapas (m_nom)VALUES("{mapa}")'
    cursor.execute(q)
    dbb.commit()
    print ("<center><h4>MAPA CREADO CORRECTAMENTE")
    print ('<form method="post" action="menu_mapas.py">')
    print (userpas)
    print ('<input type="submit" value="VOLVER" />')
    print ("</form><br></h4></center>")
else:	
	print ("USUARIO O CLAVE INCORRECTOS<br>")
	print ("---> ACCESO DENEGADO <---")
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" />')
	print ("</form><br>")	
print  ("</h4></center></body></html>")
dbb.close()