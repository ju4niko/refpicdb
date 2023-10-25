#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open('CONFIGURACION.ini').read())
exec(open("CheckPerms.py").read())
if AccesoSes(usuario,clave):

	dbb = pymysql.connect(db=DB_NAME,user=DB_USER,passwd=DB_USER_PW,host=DB_HOST)
	cursor = dbb.cursor()
	q = f'delete from ses where ses_session =\'{clave}\''
	cursor.execute(q)
	dbb.commit()

	print ("<h3>Sesion Cerrada Correctametne</h3>")

	print ('<form method="post" action="index.html">') # <--- opner aqui donde volver
	print ('<input type="submit" value=" <<< VOLVER a Login" />')
	print ("</form>")

else:
	print ("USUARIO O CLAVE INCORRECTOS<br>")
	print ("---> ACCESO DENEGADO <---")
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" />')
	print ("</form><br>")
print  ("</h4></center></body></html>")
