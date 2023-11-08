#!/usr/bin/python3
# -*- coding: utf-8 -*-
import CGoogleMapsHelper as GMH
exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave):
    limite_disp = form.getvalue('limite_disp')
    verDisp = form.getvalue('verDisp')
    mapas = form.getvalue('mapas')
    mapa = mapas.split(":")[0]
    map_id = mapas.split(":")[1]
    b = form.getvalue("bando")

    if b !=None:
        bando = b.split(":")[0]
        b_id = b.split(":")[1]
    else:
        b_id = None


    print (f'<h3> MAPA: {mapa}</h3>')

    q = f'select * from mapas where m_nom = "{mapa}"'
    cursor.execute(q)
    r = cursor.fetchone()
    dbb.commit()
    m_id = r[0]
    m_lat = r[4]
    m_lon = r[5]

    if r[0] == None:
        print(f'MAPA INEXISTNTE!')
    else:

        #print("<button onclick=\"goBack()\">Retroceder</button>")
        print('    <div id="map" style="height: 800px; width: 100%;"></div>')
        print(f'    <script src="https://maps.googleapis.com/maps/api/js?key={API_KEY}"></script>')
        print("    <script>")
       # print("function goBack() {")
       # print("    window.history.back();")
       # print("}")
        print("      function initMap() {")
        print(f'        var map = new google.maps.Map(document.getElementById("map"), {{')
        print("          zoom: 18,")
        print(f'          center: {{ lat: {m_lat:.6f}, lng: {m_lon:.6f} }},')
        print("          mapTypeId: google.maps.MapTypeId.SATELLITE")
        print("        });")

        #creo objeto para agregar items al mapa
        gmaps = GMH.GoogleMapsHelper()
        q = f'SELECT objetos.*,bandos.b_name,tipos.* FROM objetos JOIN bandos ON objetos.b_id = bandos.b_id JOIN tipos ON objetos.t_id = tipos.t_id where objetos.m_id={m_id}'

        t = cursor.execute(q)
        r = cursor.fetchall()
        
        BCOLOR = "#FF0000"
        for i in range(t):
            la = float(r[i][2])
            lo = float(r[i][3])
            bando = r[i][4]
            bando_nom = r[i][6]
            t_name = r[i][8]
            t_grosor =r[i][9]
            t_size = r[i][10]
            t_id = r[i][7]
            if  bando == 1: 
                BCOLOR = GMH.POI_A
            if bando == 2: 
                BCOLOR = GMH.POI_B
            if bando == 3: 
                BCOLOR = GMH.AMARILLO
            if bando == 4: 
                BCOLOR = "#00FF00" #verde

            if t_id in [1,2,5] : gmaps.add_square(la,lo,t_size,BCOLOR,BCOLOR)
            if t_id in [3,4]: gmaps.add_circle(la,lo,t_size,BCOLOR,BCOLOR)
            gmaps.add_text_label(la,lo,f'{t_name} {bando_nom}')

        filtrobando =''
        filtrolimite = ''
        if b_id != None: filtrobando = f' and disparo.b_id = {b_id} '
        if limite_disp != None: filtrolimite = f' limit {limite_disp} '

        if verDisp == "1":
            #ahora me fijo si hay disparos para mostrar
            t = cursor.execute(f'select distinct disparo.*, ammo.a_ratio from disparo join ammo on disparo.w_id = ammo.a_weapon where disparo.m_id = {m_id} {filtrobando} order by disparo.d_time desc {filtrolimite}')
            r = cursor.fetchall()
            if r == None:
                print()
            else:
                for i in range(t):
                    gmaps.add_text_label( (r[i][1]+r[i][3])/2 ,(r[i][2]+r[i][4])/2, f'{r[i][10]}m' )
                    gmaps.add_flecha(r[i][1],r[i][2],r[i][3],r[i][4])
                    gmaps.add_circle(r[i][3],r[i][4],r[i][11])    

        print(gmaps.generate_js_code())
        print("      }")
        print("    </script>")
        print("    <script>")
        print("      initMap();")
        print("    </script>")
        #print (f'<H2>QUERY:{r}</H2>')

    print ('<form method="post" action="menu_mapas.py">') # <--- opner aqui donde volver
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