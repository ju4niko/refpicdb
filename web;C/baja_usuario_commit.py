#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open('CONFIGURACION.ini').read())
exec(open("CheckPerms.py").read())
userdebaja = form.getvalue('userdebaja')
#print(userdebaja)
if AccesoSes(usuario,clave) and AccesoAdmin(usuario):  

	dbb = pymysql.connect(db=DB_NAME,user=DB_USER,passwd=DB_USER_PW,host=DB_HOST)
	cursor = dbb.cursor()				
	q = f"delete from users where users_nom = \'{userdebaja}\'"
	cursor.execute(q)
	dbb.commit()
	print ("<center><h4> BAJA EXITOSA")
	#print(q)
	print ('<form method="post" action="baja_usuario.py">')
	print (userpas)
	print ('<input type="submit" value="VOLVER" >')
	print ("</form><br></h4></center>")
    
else:	
	print ("<h4><center>")
	print (f"<h2>Sistema {format(SYS_NAME)} </h2><h3>Usuario: {usuario}</h3>")
	print ("<hr size=\"8px\" color=\"black\" /><h4>")	
	print ("USUARIO O CLAVE INCORRECTOS<br>")
	print ("---> ACCESO DENEGADO <---")
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" >')
	print ("</form><br></h4></center>")	
	
print  ("</body></html>")
