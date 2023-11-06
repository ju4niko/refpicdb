#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime, sys, re, random, math
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import BaseDocTemplate, SimpleDocTemplate, Paragraph, Table, Frame, PageTemplate,TableStyle, PageBreak
from html import escape
from reportlab.lib.units import inch
from reportlab.lib.units import cm

BOMBAZO="#FF0000"
BOMBAZO_FILL="#8F0000"
POI_A="#FF00FF"
POI_A_FILL="#7F007F"
POI_B="#00FFFF"
POI_B_FILL="#6F6F00"
AMARILLO="#FFFF00"
BCOLOR = ""
################################################################################
################################################################################
class GoogleMapsHelper:
    def __init__(self):
        self.objects = []

    def add_circle(self, lat, lng, radius, stroke_color=BOMBAZO, fill_color=BOMBAZO_FILL, stroke_opacity=0.8, fill_opacity=0.35):
        circle = {
            "type": "circle",
            "lat": lat,
            "lng": lng,
            "radius": radius,
            "stroke_color": stroke_color,
            "fill_color": fill_color,
            "stroke_opacity": stroke_opacity,
            "fill_opacity": fill_opacity,
        }
        self.objects.append(circle)

    def add_text_label(self, lat, lng, content):
        text_label = {
            "type": "text_label",
            "lat": lat,
            "lng": lng,
            "content": content,
        }
        self.objects.append(text_label)

    def add_marker(self, lat, lng, valor):
        marker = {
            "type": "marker",
            "lat": lat,
            "lng": lng,
            "label": valor,
        }
        self.objects.append(marker)

    def add_line(self,x0,y0,x1,y1,color,grosor):
        linea = {
            "type": "linea",
            "x0": x0,
            "y0": y0,
            "x1": x1,
            "y1": y1,
            "stroke_color": color,
            "grosor": grosor,
        }
        self.objects.append(linea)

    def add_flecha(self,x0,y0,x1,y1,color=AMARILLO,grosor=5):
        linea = {
            "type": "linea",
            "x0": x0,
            "y0": y0,
            "x1": x1,
            "y1": y1,
            "stroke_color": color,
            "grosor": grosor,
        }
        self.objects.append(linea)

    def add_square(self, lat, lng, size, stroke_color=POI_A, fill_color=POI_A, stroke_opacity=0.8, fill_opacity=0.35):


        square = {
            "type": "square",
            "lat": lat,
            "lng": lng,
            "size": size/55560,
            "stroke_color": stroke_color,
            "fill_color": fill_color,
            "stroke_opacity": stroke_opacity,
            "fill_opacity": fill_opacity,
        }
        self.objects.append(square)


    def generate_js_code(self):
        js_code = []
        for obj in self.objects:
            if obj["type"] == "circle":
                js_code.append(f'new google.maps.Circle({{')
                js_code.append(f'  strokeColor: "{obj["stroke_color"]}",')
                js_code.append(f'  strokeOpacity: {obj["stroke_opacity"]},')
                js_code.append('  strokeWeight: 2,')
                js_code.append(f'  fillColor: "{obj["fill_color"]}",')
                js_code.append(f'  fillOpacity: {obj["fill_opacity"]},')
                js_code.append(f'  map: map,')
                js_code.append(f'  center: {{ lat: {obj["lat"]:.6f}, lng: {obj["lng"]:.6f} }},')
                js_code.append(f'  radius: {obj["radius"]}')
                js_code.append('});')
            elif obj["type"] == "text_label":
                js_code.append(f'var centerLatLng = new google.maps.LatLng({obj["lat"]:.6f}, {obj["lng"]:.6f});')
                js_code.append("var textoEnCentro = new google.maps.InfoWindow({")
                js_code.append(f'  content: "{obj["content"]}",')
                js_code.append("});")
                js_code.append("textoEnCentro.setPosition(centerLatLng);")
                js_code.append("textoEnCentro.open(map);")
            elif obj["type"] == "marker":
                js_code.append(f'new google.maps.Marker({{')
                js_code.append(f' position: {{ lat: {obj["lat"]:.6f}, lng: {obj["lng"]:.6f} }},')
                js_code.append(f'  map: map,')
                js_code.append(f'  label: "{obj["label"]}"')
                js_code.append('});')
            elif obj["type"] == "linea" or obj["type"] == "flecha":
                js_code.append("        var flightPath = new google.maps.Polyline({")
                js_code.append("          path: [")
                js_code.append(f'            {{ lat: {obj["x0"]:.6f}, lng: {obj["y0"]:.6f} }},')
                js_code.append(f'            {{ lat: {obj["x1"]:.6f}, lng: {obj["y1"]:.6f} }},')
                js_code.append("          ],")
                js_code.append("          geodesic: true,")
                if obj["type"] == "flecha":
                    js_code.append("          icons: [{")
                    js_code.append('            icon: { path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW },')
                    js_code.append("            offset: '100%',")
                    js_code.append("          }],")
                js_code.append(f'  strokeColor: "{obj["stroke_color"]}",')
                js_code.append(f'  strokeWeight: {obj["grosor"]},')
                js_code.append("        });")
                js_code.append("        flightPath.setMap(map);")
            elif obj["type"] == "square":
                half_size = obj["size"] / 2
                js_code.append(f'new google.maps.Rectangle({{')
                js_code.append(f'  strokeColor: "{obj["stroke_color"]}",')
                js_code.append(f'  strokeOpacity: {obj["stroke_opacity"]},')
                js_code.append(f'  fillColor: "{obj["fill_color"]}",')
                js_code.append(f'  fillOpacity: {obj["fill_opacity"]},')
                js_code.append(f'  map: map,')
                js_code.append(f'  bounds: {{')
                js_code.append(f'    north: {obj["lat"] + half_size:.6f},')
                js_code.append(f'    south: {obj["lat"] - half_size:.6f},')
                js_code.append(f'    east: {obj["lng"] + half_size:.6f},')
                js_code.append(f'    west: {obj["lng"] - half_size:.6f}')
                js_code.append('  }')
                js_code.append('});')

        return "\n".join(js_code)
################################################################################




exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave):
    limite_disp = form.getvalue('limite_disp')
    verDisp = form.getvalue('verDisp')
    mapas = form.getvalue('mapas')
    mapa = mapas.split(":")[0]
    map_id = mapas.split(":")[1]


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
        gmaps = GoogleMapsHelper()
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
                BCOLOR = POI_A
            if bando == 2: 
                BCOLOR = POI_B
            if bando == 3: 
                BCOLOR = AMARILLO
            if bando == 4: 
                BCOLOR = "#00FF00" #verde

            if t_id in [1,2,5] : gmaps.add_square(la,lo,t_size,BCOLOR,BCOLOR)
            if t_id in [3,4]: gmaps.add_circle(la,lo,t_size,BCOLOR,BCOLOR)
            gmaps.add_text_label(la,lo,f'{t_name} {bando_nom}')
        if verDisp == "1":
            #ahora me fijo si hay disparos para mostrar
            t = cursor.execute(f'select distinct disparo.*, ammo.a_ratio from disparo join ammo on disparo.w_id = ammo.a_weapon where disparo.m_id = {m_id} order by disparo.d_time desc limit {limite_disp}')
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