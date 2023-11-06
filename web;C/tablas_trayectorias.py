#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open("CheckPerms.py").read())
if AccesoSes(usuario,clave):
    print ("<h3> TABLAS DE TRAYECTORIAS BALISTICAS por VELOCIDAD </h3>")
    cursor.execute('select a_name, a_vi from ammo order by a_vi asc')
    for a_name,a_vi in cursor.fetchall():
        print(f'<img src="iconos/{a_vi}.png" alt="Imagen Centrada {a_vi}">')

    print ('<br><br><form method="post" action="menuppal.py">') # <--- opner aqui donde volver
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