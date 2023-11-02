#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave):
	print ("<h3> MENU MAPAS </h3>")
	
	print ('<hr> <form name="myForm"  method="post" action="VerMapa.py"> ')
	print (userpas)
	print ('Mapa:<input type="text" name="mapa" id="mapa" value="" maxlenght="20" autocomplete="off" size="20" ><br>')
	print (' <input type="submit" value="> Ver Mapa <" /><br>')
	print ("</form> ")
	

	if AccesoAdmin(usuario):

		
		print ("<hr> <form method=\"post\" action=\"edit_map.py\">")
		print (userpas)

		print (f'  <h4>Mapa:<input list="mapa" name="mapa"><datalist id="mapa">')
		q = f'select m_nom,m_id from mapas'
		tot=cursor.execute(q)
		r = cursor.fetchall()
		for f in list(range(tot)):
			print(f'<option value="{r[f][0]}:{r[f][1]}">')
		print('  </datalist></h4>')
 
		print ("<input type=\"submit\" value=\"> Editar Mapa <\" />")
		print ("</form> ")

		
		if AccesoSuAdmin(usuario):
			print ('<hr> <form method="post" action="create_mapa_commit.py"> ')
			print (userpas)
			print ('Mapa:<input type="text" name="mapa" id="mapa" value="" maxlenght="20" autocomplete="off" size="20" ><br>')
			print (' <input type="submit" value="> Nuevo Mapa <" /><br>')
			print ("</form> ")
			
			print ("<hr> <form method=\"post\" action=\"delete_map.py\">")
			print (userpas)
			print ('Mapa:<input type="text" name="mapa" id="mapa" value="" maxlenght="20" autocomplete="off" size="20" ><br>')
			print ("<input type=\"submit\" value=\"> Borrar Mapa <\" />")
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
cursor.close()
dbb.close()