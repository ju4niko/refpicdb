#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open("CheckPerms.py").read())

if AccesoSuAdmin(usuario):
	print ("<h3> CREAR EVENTO </h3>")
	evento = form.getvalue('evento')
	print('<form method="post" action="create_evento_commit.py">')
	print('<div style="margin: 10 auto; width: 300px;">')  # Establece el ancho y el centrado del contenedor.
	print(f'<h4>{evento}</h4>')
	print(f'    <label for="fecha">Fecha:</label>')
	print(f'    <input type="date" id="fecha" name="fecha" required><br><br>')
	print(f'    <label for="facciones">Facciones:</label>')
	print(f'    <input type="number" id="facciones" name="facciones" required><br><br>')
	print(f'    <input type="submit" value="CREAR!">')
	print(f'    <input type="hidden" id="evento" name="evento" value="{evento}">')
	print (userpas)

	
	print('</div>')  # Cierra el contenedor.
	print("</form>")

else:	
	print ("USUARIO O CLAVE INCORRECTOS<br>")
	print ("---> ACCESO DENEGADO <---")
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" />')
	print ("</form><br>")	
print  ("</h4></center></body></html>")
dbb.close()