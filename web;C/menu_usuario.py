#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open('CONFIGURACION.ini').read())
exec(open("CheckPerms.py").read())
if AccesoSes(usuario,clave):
	print ("<h3>Operaciones de Usuarios</h3>")
	print ("<form method=\"post\" action=\"cambia_pass.py\">")
	print (userpas)
	print ("<input type=\"submit\" value=\"> Cambio de Clave <\" />")
	print ("</form>")
	if AccesoSuAdmin(usuario):
		print ("<form method=\"post\" action=\"useradmin.py\">")
		print (userpas)
		print ("<input type=\"submit\" value=\"> Admin. de usuarios <\" >")
		print ("</form>")
	print ('<form method="post" action="menuppal.py">') # <--- opner aqui donde volver
	print (userpas)
	print ('<input type="submit" value=" <<< VOLVER" >')
	print ("</form>")
    
else:		
	print (GetOutOfHere)

print  ("</h4></center></body></html>")
dbb.close()
