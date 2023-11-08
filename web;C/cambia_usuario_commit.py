#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave) and AccesoAdmin(usuario):
    username = form.getvalue('username')
    b = form.getvalue('bando')
    habilitado = form.getvalue('habilitado')
    uc = form.getvalue('usercat')
    due = form.getvalue('due')
 
    if habilitado == None: habilitado = 0
    else: habilitado = 1
    if due == None: usersdue = ' users_due = NULL , '
    else: usersdue = f'users_due = "{due}" , '

    if b == None: bandid = ' b_id = NULL , '
    else: bandid = f' b_id = {b.split(":")[1]} , '

    if uc == None: usercat = ' '
    else: usercat = f' users_cat = "{uc.split(":")[1]}" , '

    q = f'update users set {bandid} {usercat} {usersdue} users_enable = {habilitado} where users_nom = "{username}" '

#    print (f'{q} ')    
    cursor.execute(q)
    dbb.commit()
    print ("<center><h4>USUARIO MODIFICADO CORRECTAMENTE")
    print ('<form method="post" action="cambia_usuario.py">')
    print (userpas)
    print ('<input type="submit" value="VOLVER" />')
    print ("</form><br></h4></center>")
else:	
	print ("<h4><center>")
	print (f"<h2>Sistema {format(SYS_NAME)} </h2><h3>Usuario: {usuario}</h3>")
	print ("<hr size=\"8px\" color=\"black\" /><h4>")	
	print ("USUARIO O CLAVE INCORRECTOS<br>")
	print ("---> ACCESO DENEGADO <---")
	print ('<form method="post" action="index.html">')
	print ('<input type="submit" value="VOLVER" />')
	print ("</form><br></h4></center>")	
	
print  ("</body></html>")
cursor.close()
dbb.close()  