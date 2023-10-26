#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave):
	print ("<h3> MENU EVENTOS </h3>")
	
	print ('<hr> <form name="myForm"  method="post" action="VerEvento.py"> ')
	print (userpas)
	print ('Evento:<input type="text" name="evento" id="evento" value="" maxlenght="20" autocomplete="off" size="20" ><br>')
	print (' <input type="submit" value="> Ver Evento <" /><br>')
	print ("</form> ")
	

	if AccesoAdmin(usuario):

		
		print ("<hr> <form method=\"post\" action=\"edit_event.py\">")
		print (userpas)
		print ('Evento:<input type="text" name="evento" id="evento" value="" maxlenght="20" autocomplete="off" size="20" ><br>')
		print ("<input type=\"submit\" value=\"> Editar Evento <\" />")
		print ("</form> ")

		
		if AccesoSuAdmin(usuario):
			print ('<hr> <form method="post" action="create_evento.py"> ')
			print (userpas)
			print ('Evento:<input type="text" name="evento" id="evento" value="" maxlenght="20" autocomplete="off" size="20" ><br>')
			print (' <input type="submit" value="> Nuevo Evento <" /><br>')
			print ("</form> ")
			
			print ("<hr> <form method=\"post\" action=\"delete_evento.py\">")
			print (userpas)
			print ('Evento:<input type="text" name="evento" id="evento" value="" maxlenght="20" autocomplete="off" size="20" ><br>')
			print ("<input type=\"submit\" value=\"> Borrar evento <\" />")
			print ("</form> ")
	print ('<form method="post" action="menuppal.py">') # <--- opner aqui donde volver
	print (userpas)
	print ('<input type="submit" value=" <<< VOLVER" >')
	print ("</form>")  

    
  
else:	
	print ("USUARIO O CLAVE INCORRECTOS<br>")
	print ("---> ACCESO DENEGADO <---")
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" />')
	print ("</form><br>")	
print  ("</h4></center></body></html>")
dbb.close()