#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open('CONFIGURACION.ini').read())
exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave) and AccesoAdmin(usuario):     

	dbb = pymysql.connect(db=DB_NAME,user=DB_USER,passwd=DB_USER_PW,host=DB_HOST)
	cursor = dbb.cursor()
	q = f"SELECT users_nom FROM users where users_nom <> \"{usuario}\""
	tot = cursor.execute(q)
	r = cursor.fetchall()

	print ('<h3>Baja de Usuario ')

	print ('<form action="baja_usuario_commit.py" method="post" id = "baja_de_user" >')	
	print ('Usuario: <input type="text"  name="userdebaja" >')
	
	print (userpas)	
	print ('<input type="submit" value="> BAJA <" >')
	print ('</form>')
	

#	print ('<br>Usuario: <select name="userdebaja" form="baja_de_user" >')
#	for i in list(range(tot)):
#		print (f"<option value>{r[i][0]}</option>")
#	print ('</select>')
	

	print ('</h3><hr><br>')    
	print ('<form method="post" action="AyudaSys.py">')
	print (userpas)
	print ('<input type="submit" value="Ver AYUDA" />')
	print ('</form>')
	print ('<form method="post" action="useradmin.py">') # <--- opner aqui donde volver
	print (userpas)
	print ('<input type="submit" value=" <<< VOLVER" />')
	print ('</form>')
else:	
	print ('USUARIO O CLAVE INCORRECTOS<br>')
	print ('---> ACCESO DENEGADO <---')
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" />')
	print ('</form><br>')	
print  ('</h4></center></body></html>')