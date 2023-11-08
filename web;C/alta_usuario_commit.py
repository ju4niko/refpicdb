#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open("CheckPerms.py").read())

def encrip(pw):
	return pw #desactivado por ahora
	
	# aca enrroscar la clave
	import base64
	from Crypto.Cipher import AES
	p = pw.rjust(32)
	seckey = b'2212592520200448'
	chipher = AES.new(seckey,AES.MODE_ECB)
	return base64.b64encode(chipher.encrypt(p))



username = form.getvalue('username')
pass1 = form.getvalue('pass1')
pass2 = form.getvalue('pass2')
usercat = form.getvalue('usercat')
#print (usercat,pass1,pass2,username)
userpas = f"<input type=\"hidden\" name=\"usuario\" value=\"{usuario}\" id=\"usuario\" >  <input type=\"hidden\" name=\"clave\" value=\"{clave}\" id=\"clave\" >"


if AccesoSes(usuario,clave) and AccesoAdmin(usuario):  
	if (pass1 == pass2) and (pass1 != None) and (username != None):
		q = f'insert into users (users_nom, users_pwd, users_cat) values ("{username}","{encrip(pass1)}","{usercat}")'
		#print(q)
		cursor.execute(q)
		dbb.commit()
		
		print ("<center><h4>USUARIO CREADO CORRECTAMENTE")
		print ('<form method="post" action="alta_usuario.py">')
		print (userpas)
		print ('<input type="submit" value="VOLVER" />')
		print ("</form><br></h4></center>")
	else:
		print ("<center><h4>CLAVES NO COINCIDEN o USUARIO ERRONEO")
		print ('<form method="post" action="alta_usuario.py">')
		print (userpas)
		print ('<input type="submit" value="VOLVER" />')
		print ("</form><br></h4></center>")

else:	
	print ("<h4><center>")
	print (f"<h2>Sistema {format(SYS_NAME)} </h2><h3>Usuario: {usuario}</h3>")
	print ("<hr size=\"8px\" color=\"black\" /><h4>")	
	print ("USUARIO O CLAVE INCORRECTOS<br>")
	print ("---> ACCESO DENEGADO <---")
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" />')
	print ("</form><br></h4></center>")	
	
print  ("</body></html>")
cursor.close()
dbb.close()  