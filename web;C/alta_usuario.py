#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open('CONFIGURACION.ini').read())
exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave) and AccesoAdmin(usuario):     
	print ('<h3>Creacion de Usuario Comlpete todos los campos</h3>')
	print ('<form action="alta_usuario_commit.py" method="post" id="usrnam">')
	print (userpas)
	print ('<h3>-Nombre de usuario: <input type="text" name="username"   >')
	print ('<br>-----------> Clave: <input type="password" name="pass1"  id="usrpas1" >')
	print ('<br>--Reingresar clave: <input type="password" name="pass2"  id="usrpas2" ><br>')
	print ('<input type="radio" name="usercat" value="U"> Operador')
	print ('<input type="radio" name="usercat" value="A"> Administrador <br>')	
	print ('<br><input type="submit" value="> ALTA <" >')
	print ('</form>')
	
#	print ('<br>---Nivel de acceso: <select name="usercat" form="usrnam" >')
#	print ('<option value>--------Operador---------</option>')
#	print ('<option value>------Administrador------</option>')
#	print ('</select>')
	
	print ('</h3>')
	
	
	print ('<hr><br>')    
	
	print ('<form method="post" action="AyudaSys.py">')
	print (userpas)
	print ('<input type="submit" value="Ver AYUDA" >')
	print ('</form>')
	
	print ('<form method="post" action="useradmin.py">') # <--- opner aqui donde volver
	print (userpas)
	print ('<input type="submit" value=" <<< VOLVER" >')
	print ('</form>')
else:	
	print ('USUARIO O CLAVE INCORRECTOS<br>')
	print ('---> ACCESO DENEGADO <---')
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" >')
	print ('</form><br>')	
print  ('</h4></center></body></html>')