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

        print(f'    <label for="objeto">Objeto:</label>')
        print(f'    <input type="text" id="objeto" name="objeto" required><br><br>')

        print(f'    <label for="facciones">Facciones:</label>')
        print(f'    <input type="number" id="facciones" name="facciones" required><br><br>')

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
dbb.close()