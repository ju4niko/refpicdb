#!/usr/bin/python3
# -*- coding: utf-8 -*-

exec(open("CheckPerms.py").read())

if AccesoSes(usuario,clave):

    map_id = form.getvalue('map_id')

    b = form.getvalue("bando")
    w = form.getvalue("weapon")
    a = form.getvalue("ammo")
    p1 = form.getvalue('latlon')
    e = form.getvalue("elevacion")
    z = form.getvalue("azimut")


    bando = b.split(":")[0]
    b_id = b.split(":")[1]

    weapon = w.split(":")[0] 
    w_id = w.split(":")[1]

    a = a.split(":")[0] 
    a_id = a.split(":")[1]

    e = e.split(":")[0] 
    e_id = e.split(":")[1]

    z = z.split(":")[0] 
    z_id = z.split(":")[1]

    latlon = p1.split(",")

    html = """
        <script>
            window.onload = function() {
                // Redirige a la URL deseada después de que la página se haya cargado
                window.location.href = 'https://www.ejemplo.com/otra-pagina';
            };
        </script>
    """
    print(html)
