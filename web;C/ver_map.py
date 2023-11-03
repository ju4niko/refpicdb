#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open("CheckPerms.py").read())




if AccesoSes(usuario,clave):
	print (f'<h3> MENU: {mapa}</h3>')

    mapas = form.getvalue('mapas')
    mapa = mapas.split(":")[0]
    map_id = mapas.split(":")[1]
    
    q = f'select m_id from mapas where m_nom = "{mapa}"'
    cursor.execute(q)
    r = cursor.fetchone()
    dbb.commit()
    if r == None:
        print(f'MAPA INEXISTNTE!')
    else:



	
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