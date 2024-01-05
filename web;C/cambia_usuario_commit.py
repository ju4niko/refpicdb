#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave) and AccesoAdmin(usuario):
    username = form.getvalue('username')
    b = form.getvalue('bando')
    m = form.getvalue('mapa')
    habilitado = form.getvalue('habilitado')
    uc = form.getvalue('usercat')
    due = form.getvalue('due')
    aw = form.getvalue('assignedw')
 


    if habilitado == None: habilitado = 0
    else: habilitado = 1
    if due == None: usersdue = ' users_due = NULL , '
    else: usersdue = f'users_due = "{due}" , '

    if b == None: bandid = ' b_id = NULL , '
    else: bandid = f' b_id = {b.split(":")[1]} , '
    if m == None: mapid = ' m_id = NULL , '
    else: mapid = f' m_id = {m.split(":")[1]} , '

    if uc == None: usercat = ' '
    else: 
        ucat = uc.split(":")[1]
        usercat = f' users_cat = "{ucat}" , '
        if ucat != "U" and ucat != "A" and ucat != "S" and ucat != "P":
            print ("<center><h4>NO EXISTE LA CATEGORIA DE USUARIO INGRESADA</h4>")
        else:
            q = f'update users set {bandid} {usercat} {usersdue} {mapid} users_enable = {habilitado} where users_nom = "{username}" '   
            #print (q)
            cursor.execute(q)
            dbb.commit()

            if aw != None: 
                w_id = f'{aw.split(":")[1]}'
                u_id = getIDfromTable("users_id","users","users_nom",username)
                cursor.execute(f'insert into assign_w (users_id,w_id)values({u_id},{w_id})')
                dbb.commit()
            print ("<center><h4>USUARIO MODIFICADO CORRECTAMENTE</h4>")




    print ('<form method="post" action="useradmin.py">')
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