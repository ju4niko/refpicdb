#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open('CONFIGURACION.ini').read())
exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave) and AccesoAdmin(usuario):     
	print ('<h3>Creacion de Usuario Comlpete todos los campos</h3>')
	print ('<form action="alta_usuario_commit.py" method="post" id="usrnam">')
	print('<table>')

	print('<tr>')
	print('<td style="text-align: right;padding: 5px;">Nombre de usuario:</td>')
	print('<td style="padding: 5px;"><input type="text" name="username"    required="True" ></td>')
	print('</tr>')

	print('<tr>')
	print('<td style="text-align: right;padding: 5px;">Categoria:</td>')
	print('<td style="padding: 5px;"><input list="usercat" name="usercat" required="True" ><datalist id="usercat">')
	print(f'<option value="Administrador:A">')
	print(f'<option value="Usuario:U">')
	print(f'<option value="Jugador:P">')
	print('</datalist></td>')
	print('</tr>')

#	print('<tr>')
#	print('<td style="text-align: right;padding: 5px;">Bando:</td>')
#	print('<td style="padding: 5px;"><input list="bando" name="bando"><datalist id="bando">')
#	cursor.execute('select b_name, b_id from bandos order by b_name asc')
#	for b_name, b_id in cursor.fetchall(): print(f'<option value="{b_name}:{b_id}">')
#	print('</tr>')


#	print('<tr>')
#	print('<td style="text-align: right;padding: 5px;">Mapa:</td>')
#	print('<td style="padding: 5px;"><input list="mapa" name="mapa"><datalist id="mapa">')
#	cursor.execute('select m_nom, m_id from mapas order by m_nom asc')
#	for m_name, m_id in cursor.fetchall(): print(f'<option value="{m_name}:{m_id}">')
#	print('</datalist></td>')
#	print('</tr>')

#	print('<tr>')
#	print('<td style="text-align: right;padding: 5px;">Armamento asignado:</td>')
#	print('<td style="padding: 5px;"><input list="assignedw" name="assignedw"><datalist id="assignedw">')
#	cursor.execute('select w_name, w_id from weapon order by w_name asc')
#	for w_name, w_id in cursor.fetchall(): print(f'<option value="{w_name}:{w_id}">')
#	print('</datalist></td>')
#	print('</tr>')


#	print('<tr>')
#	print('<td style="text-align: right;padding: 5px;">Habilitado:</td>')
#	print('<td style="padding: 5px;">\
#		<input \
#		type="checkbox" \
#		name="habilitado" \
#		id="habilitado" \
#		></td>')
#	print('</tr>')

#	print('<tr>')
#	print('<td style="text-align: right;padding: 5px;">Fecha Validez:</td>')
#	print('<td style="padding: 5px;">')
#	print(f'    <input type="date" id="due" name="due" >')
#	print('</td></tr>')

	print('<tr>')
	print('<td style="text-align: right;padding: 5px;">Clave:</td>')
	print('<td style="padding: 5px;">')
	print('<input type="password" name="pass1"  id="usrpas1"  required="True" >')
	print('</td></tr>')

	print('<tr>')
	print('<td style="text-align: right;padding: 5px;">Reingrese Clave:</td>')
	print('<td style="padding: 5px;">')
	print('<input type="password" name="pass2"  id="usrpas2" required="True" >')
	print('</td></tr>')
	
	print('</table>')

	print (userpas)
	print ('<input type="submit" value=" CREAR " />')
	print ("</form>")

	
	print ('<hr><br>')    
	
	print ('<form method="post" action="AyudaSys.py">')
	print (userpas)
	print ('<input type="submit" value="Ver AYUDA" >')
	print ('</form>')
	
	print ('<form method="post" action="useradmin.py">') # <--- opner aqui donde volver
	print (userpas)
	print ('<input type="submit" value=" <<< VOLVER" >')
	print ('</form>')
else:	
	print ('USUARIO O CLAVE INCORRECTOS<br>')
	print ('---> ACCESO DENEGADO <---')
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" >')
	print ('</form><br>')	
print  ('</h4></center></body></html>')