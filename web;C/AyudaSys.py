#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open('CONFIGURACION.ini').read())
exec(open("CheckPerms.py").read())
if AccesoSes(usuario,clave):

	print ("<h3>Ayuda del Sistema</h3>")
	print ('</center><h4><hr>')

	print (' 	- El sistema tiene 3 niveles de usuario: SuperAdmin, Admin, Operador <br>')
	print (' 	- El operador solo puede hacer consultar<br>')
	print (' 	- El usuario Administrador puede hacer modificaciones salvo <br>')
	print (' 	- crear usuarios, pedir reportes.etc <br>')
	print (' 	- El SuperAdmin puede hacer todo incluido administrar usuarios <br>')
	print (' 	- y otras funcinoes especiales <br>')
	print (' 	- ..... en construccion.... <br>')
	print (' 	-  <br>')

	print ('<br>')
	print ('<hr></h4><center>')
	#opcion
	print ('<form method="post" action="menuppal.py">')
	print (userpas)
	print ('    <input type="submit" value="<<< VOLVER" /></form>')
else:
    print ('<h3>ACCESO DENEGADO</h3>')
print ('</center></body></html>\n\r')
