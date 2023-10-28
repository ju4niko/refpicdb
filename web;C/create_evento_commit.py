#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open("CheckPerms.py").read())

if AccesoSuAdmin(usuario):    
    evento = form.getvalue('evento')
    fecha = form.getvalue('fecha')
    facciones = form.getvalue('facciones')
    q = f'INSERT INTO eventos (e_nom, e_fecha, e_bandos)VALUES("{evento}","{fecha}",{facciones})'
    cursor.execute(q)
    dbb.commit()
    print ("<center><h4>EVENTO CREADO CORRECTAMENTE")
    print ('<form method="post" action="menu_eventos.py">')
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