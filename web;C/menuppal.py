#!/usr/bin/python3
# -*- coding: utf-8 -*-

print('Content-Type:text/html;charset=utf-8\r\n')
print('\r\n')

exec(open('CONFIGURACION.ini').read())
exec(open("CheckPerms.py").read())
inicio = form.getvalue('inicio')
test1 = form.getvalue('test1')
acceder = False
if str(inicio) == str("inicio"):
	acceder = Acceso(usuario,clave)
	if acceder:
		dbb = pymysql.connect(db=DB_NAME,user=DB_USER,passwd=DB_USER_PW,host=DB_HOST)
		cursor = dbb.cursor()
	#borro sesiones anteriores
		q = f"delete from ses where ses_users_nom = \"{usuario}\""
		cursor.execute(q)
		dbb.commit()
	#creo ses id nuevo
		clave = uuid.uuid4()
		q = f"insert into ses (ses_session, ses_users_nom) values(\'{clave}\',\'{usuario}\')"
		cursor.execute(q)
		dbb.commit()
		userpas = f'<input type="hidden" name="usuario" value="{usuario}" id="usuario" >  \
					<input type="hidden" name="clave" value="{clave}" id="clave" >'

else:
	acceder = AccesoSes(usuario,clave)

if acceder:
	print ("<h3>MENU PRINCIPAL</h3>")

	print ("<form method=\"post\" action=\"deposito.py\"  >")
	print (userpas)
	print ("<input type=\"submit\" value=\"> Deposito <\" />")
	print ("</form>")


	print ('<form method="post" action="menu_usuario.py" >')
	print (userpas)
	print ('<input type="submit" value=">  Operac. Usuario  <" />')
	print ('</form>')
	if AccesoAdmin(usuario):
		print ('<hr><h4><form name="myForm" onsubmit="return validateForm()" method="post" action="DespachoPedido.py"><pre>')
		print (userpas)
		print ('Pedido:<input type="text" name="npedido" id="npedido" value="" maxlenght="6" autocomplete="off" size="6" \
			> Juntar con:<input type="text" name="pedidofusion" id="pedidofusion" value="" maxlenght="6" autocomplete="off" size="6" ><br>')
		print ('Motivo:  <input type="text" name="motivofusion" value="" id="motivofusion" maxlenght="30" autocomplete="off" size="30" ><br>')

		print ('Cliente:        <input type="text" name="cliente" value="" maxlenght="20" autocomplete="off" size="20"><br>')
		print ('</pre><input type="submit" value="> Despacho de Pedidos <" /><br>')
		print ("</form></h4><hr>")

		if AccesoSuAdmin(usuario):
			print('<hr><h3>Baja de Stock</h3>')
			print ("<form method=\"post\" action=\"bajaEtiqueta.py\">")
			print (userpas)
			print ("<input type=\"submit\" value=\"> Baja por Codigo <\" />")
			print ("</form>")


	print ('</h4><center><hr>')
	print ('<form method="post" action="AyudaSys.py">')
	print (userpas)
	print ('<input type="submit" value="Ver AYUDA" />')
	print ("</form>")
	print (f'<form method="post" action="cierra_ses.py">')
	print (userpas)
	print ('<input type="submit" value="SALIR DEL SISTEMA!!!" />')
	print ("<hr></form>")

	print ('<script type="text/javascript">')
	print ('  function  validateForm() { ') # abre la fucion --------------->
	print('var x = document.forms["myForm"]["pedidofusion"].value;')
	print('var x1 = document.forms["myForm"]["motivofusion"].value;')
	print('if  (x1 == "" || x1 == null ) \
			{\
			if (x != "" ) \
				{\
				alert("Completar Motivo");return false;\
				}\
			}')
	#print('if (x1 == "" || x1 == null) {alert("Completar Color");return false;}')
	print('} ') #cierra la funcion <----------------------------

	#print ('  function init() {     document.getElementById("neto").focus(); document.getElementById("neto").value = ""; document.getElementById("reimprimir").checked = false;} ')
	#print ('window.onload = init; ')
	print(' </script>')

else:
	print (GetOutOfHere) #donde volver

print  ("</h4></center></body></html>")
