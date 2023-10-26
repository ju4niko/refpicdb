#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open("CheckPerms.py").read())
inicio = form.getvalue('inicio')
test1 = form.getvalue('test1')
acceder = False
if str(inicio) == str("inicio"):
	acceder = Acceso(usuario,clave)
	if acceder:
		#dbb = pymysql.connect(db=DB_NAME,user=DB_USER,passwd=DB_USER_PW,host=DB_HOST)
		#cursor = dbb.cursor()
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
	
	print ('<form method="post" action="menu_usuario.py" >')
	print (userpas)
	print ('<input type="submit" value=">  Operac. Usuario  <" />')
	print ('</form>')
	
	print ('<hr> <form name="myForm"  method="post" action="menu_mapas.py"> ')
	print (userpas)
	#print ('Mapa:<input type="text" name="mapa" id="mapa" value="" maxlenght="20" autocomplete="off" size="20" ><br>')
	print (' <input type="submit" value="> Mapas <" /><br>')
	print ("</form> ")
	
	print ('<hr> <form name="myForm"  method="post" action="menu_eventos.py"> ')
	print (userpas)
	#print ('Mapa:<input type="text" name="mapa" id="mapa" value="" maxlenght="20" autocomplete="off" size="20" ><br>')
	print (' <input type="submit" value="> Eventos <" /><br>')
	print ("</form> ")
	

#	if AccesoAdmin(usuario):

		
		
#		if AccesoSuAdmin(usuario):


	print (' <center>')
	print ('<hr><form method="post" action="AyudaSys.py">')
	print (userpas)
	print ('<input type="submit" value="Ver AYUDA" />')
	print ("</form>")
	print (f'<hr><form method="post" action="cierra_ses.py">')
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
	print('} ') #cierra la funcion <----------------------------


	print(' </script>')

else:
	print (GetOutOfHere) #donde volver

print  (" </center></body></html>")
dbb.close()
