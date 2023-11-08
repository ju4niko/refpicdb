#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open("CheckPerms.py").read())
if AccesoSes(usuario,clave) and AccesoAdmin(usuario):
    print ("<h3>Modifica Usuario Usuarios</h3>")

    print ('<form method="post" action="cambia_usuario_commit.py">') # <--- opner aqui donde volver

    print('<table>')


    print('<tr>')
    print('<td style="padding: 5px;">Usuario:</td>')
    print('<td style="padding: 5px;"><input list="username" name="username"><datalist id="username">')
    cursor.execute('select users_nom, users_id from users')
    for u_name,u_id in cursor.fetchall(): print(f'<option value="{u_name}">')
    print('</datalist></td>')
    print('</tr>')

    print('<tr>')
    print('<td style="padding: 5px;">Categoria:</td>')
    print('<td style="padding: 5px;"><input list="usercat" name="usercat"><datalist id="usercat">')
    print(f'<option value="Administrador:A">')
    print(f'<option value="Usuario:U">')
    print(f'<option value="Jugador:P">')
    print('</datalist></td>')
    print('</tr>')


    print('<tr>')
    print('<td style="padding: 5px;">Bando:</td>')
    print('<td style="padding: 5px;"><input list="bando" name="bando"><datalist id="bando">')
    cursor.execute('select b_name, b_id from bandos order by b_name asc')
    for b_name, b_id in cursor.fetchall(): print(f'<option value="{b_name}:{b_id}">')
    print('</datalist></td>')
    print('</tr>')



    print('<tr>')
    print('<td style="padding: 5px;">Habilitado:</td>')
    print('<td style="padding: 5px;">\
        <input \
        type="checkbox" \
        name="habilitado" \
        id="habilitado" \
        ></td>')
    print('</tr>')

    print('<tr>')
    print('<td style="padding: 5px;">Fecha Validez:</td>')
    print('<td style="padding: 5px;">')
    
    print(f'    <input type="date" id="due" name="due" >')
    #print(f'    <input type="checkbox" id="fechavalida" name="fechavalida">')

    print('</td></tr>')
    
    
    print('</table>')

    print (userpas)
    print ('<input type="submit" value=" MODIFICAR " />')
    print ("</form>")
 

    print ('<form method="post" action="useradmin.py">') # <--- opner aqui donde volver
    print (userpas)
    print ('<input type="submit" value=" <<< VOLVER" />')
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