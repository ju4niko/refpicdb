#!/usr/bin/python3
# -*- coding: utf-8 -*-
exec(open("CheckPerms.py").read())
if AccesoSes(usuario,clave):
    print ("<h3>EDICION DE MAPA</h3>")
 
    mapa = form.getvalue('mapa')
    q = f'select m_id from mapas where m_nom = "{mapa}"'
    cursor.execute(q)
    r = cursor.fetchone()
    dbb.commit()
    if r == None:
        print(f'MAPA INEXISTNTE!')
    else:

        print('<form method="post" action="inserta_mapa_commit.py">')
        print('<div style="margin: 10 auto; width: 300px;">')  # Establece el ancho y el centrado del contenedor.
        print(f'<h4>{mapa}</h4>')

        print (f'  <h4>Objeto:<input list="objeto" name="objeto"><datalist id="objeto">')
        q = f'select t_name,t_id from tipos order by t_name asc'
        tot = cursor.execute(q)
        r = cursor.fetchall()
        for f in list(range(tot)):
            print(f'<option value="{r[f][0]}:{r[f][1]}">')
        print('  </datalist></h4>')
        
        print (f'  <h4>Bando:<input list="bando" name="bando"><datalist id="bando">')
        q = f'select b_name,b_id from bandos order by t_name asc'
        t1 = cursor.execute(q)
        r = cursor.fetchall()
        for g in list(range(t1)):
            print(f'<option value="{r[g][0]}:{r[g][1]}">')
        print('  </datalist></h4><br>')

        print(f'    <input type="submit" value="CREAR!">')
        print(f'    <input type="hidden" id="evento" name="evento" value="{mapa}">')
        print (userpas)
        print('</div>')  # Cierra el contenedor.
        print("</form>")

    print ('<form method="post" action="menu_mapas.py">') # <--- poner aqui donde volver
    print (userpas)
    print ('<input type="submit" value=" <<< VOLVER" >')
    print ("</form>")
    
else:		
	print (GetOutOfHere)

print  ("</h4></center></body></html>")
cursor.close()
dbb.close()