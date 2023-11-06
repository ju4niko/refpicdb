#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave):
	print ("<h3> MENU MAPAS </h3>")
	
	print ('<hr> <form name="myForm"  method="post" > ')
	print (userpas)

	print (f'  <h4>Mapa:<input list="mapas" name="mapas" ><datalist id="mapas">')
	q = f'select m_nom,m_id from mapas'
	t=cursor.execute(q)
	r = cursor.fetchall()
	for i in list(range(t)):
		print(f'<option value="{r[i][0]}:{r[i][1]}">')
	print('  </datalist></h4>')

	html = """
		<style>
		table {
			border-collapse: collapse; /* Combina los bordes de las celdas */
			margin: 0 auto; /* Centrar la tabla horizontalmente */
		}

		th, td {
			text-align: center; /* Centrar el contenido de las celdas horizontalmente */
			border: 1px solid black; /* Añade un borde de 1 píxel sólido alrededor de las celdas */
			padding: 8px; /* Añade espacio interno para el contenido */
		}
		</style>

		"""
	print(html)

	print('<table><center>')
	print('<tr> <th> ACCION </th> <th> FILTROS </th> </tr>')
	print ('<tr><td> <button type="submit" formaction="ver_map.py" > Ver  </button></td>')
	
	print(f' <td> <label for="verDisp"> Disparos </label>')
	print(f' <input type="checkbox" id="verDisp" name="verDisp" value="1">')

	print(f'Cant:<input type="text" name="limite_disp" id="limite_disp" value=""> </td>')
	
	print ('<tr><td> <button type="submit" formaction="edit_map.py" > Editar  </button> </td> <td></td> </tr>')
	print ('<tr><td> <button type="submit" formaction="disparo.py" > DISPARO!  </button></td> <td></td> </tr>')


	if AccesoAdmin(usuario):
		print ('<tr><td> <button type="submit" formaction="create_mapa.py" > Crear  </button> </td> <td></td> </tr>')
		if AccesoSuAdmin(usuario):
			print ('<tr><td> <button type="submit" formaction="delete_mapa.py" > Borrar  </button></td> <td></td> </tr>')
	print ("</center></table></form> ")


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