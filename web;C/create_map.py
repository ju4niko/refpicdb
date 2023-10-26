#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open('CONFIGURACION.ini').read())
exec(open("CheckPerms.py").read())
if AccesoSes(usuario,clave) and AccesoAdmin(usuario):    
	
    print ("<h3>Seleccione Accion del Menu</h3>")
    
    print ("<form method=\"post\" action=\"alta_usuario.py\">")
    print (userpas)
    print ("<input type=\"submit\" value=\"> Alta de Usuario <\" />")
    print ("</form>")


    
else:	
	print ("USUARIO O CLAVE INCORRECTOS<br>")
	print ("---> ACCESO DENEGADO <---")
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" />')
	print ("</form><br>")	
print  ("</h4></center></body></html>")
dbb.close()