#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave):
	print ("<h3> MENU MAPAS </h3>")
	
	print ('<hr> <form name="myForm"  method="post" > ')
	print (userpas)

	print (f'  <h4>Mapa:<input list="mapas" name="mapas"><datalist id="mapas">')
	q = f'select m_nom,m_id from mapas'
	t=cursor.execute(q)
	r = cursor.fetchall()
	for i in list(range(t)):
		print(f'<option value="{r[i][0]}:{r[i][1]}">')
	print('  </datalist></h4>')
	print (' <button type="submit" formaction="ver_map.py" > Ver  </button>')
	print (' <button type="submit" formaction="edit_map.py" > Editar  </button>')

	if AccesoAdmin(usuario):
		print (' <button type="submit" formaction="create_mapa.py" > Crear  </button>')
		if AccesoSuAdmin(usuario):
			print (' <button type="submit" formaction="delete_mapa.py" > Borrar  </button>')
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