#!/usr/bin/env python3
from flask import Flask, request
import CalculoBalistico as CB
import math
#exec(open("CheckPerms.py").read())
exec(open('CONFIGURACION.ini').read())
import pymysql

app = Flask(__name__)

@app.route('/posicion', methods=['POST'])
def posicion():
    if request.method == 'POST':
        data = request.get_json()  # Accede a los datos JSON
        mapa = data.get('map-id')
        bando = data.get('team-id')
        tipo = data.get('type')
        ll = data.get('coordinates')

        latlon = ll.split(",")
        lat = latlon[0]
        lon = latlon[1]

        print (f'mapa:{mapa}')        
        print(f'bando:{bando}')
        print(f'tipo:{tipo}')
        print(f'lat:{lat},lon:{lon}')

    return "\n"

@app.route('/disparo', methods=['POST'])
def disparo():
    if request.method == 'POST':
        data = request.get_json()  # Accede a los datos JSON
        m_id = data.get('map-id')
        w_id = data.get('weapon-id') 
        a_id = data.get("ammo-id")
        b_id = data.get('team-id')
        elev = data.get('elevation')
        azimut = data.get('azimut')
        ll = data.get('coordinates')

        latlon = ll.split(",")
        lat = latlon[0]
        lon = latlon[1]

        dbb = pymysql.connect(db=DB_NAME,user=DB_USER,passwd=DB_USER_PW,host=DB_HOST)
        cursor = dbb.cursor()

        cursor.execute(f'select a_vi,a_mil from ammo where a_id = {a_id}')
        r = cursor.fetchone()
        Vi = int(r[0])
        MIL = int(r[1])
        FACTOR_MIL = float(MIL/(2*3.14159*1000))

        distancia = ((Vi ** 2 * math.sin( 2 * ( (elev/FACTOR_MIL ) /1000) )) / 9.81)
        lati, loni = CB.calc_impacto(float(lat),float(lon), azimut/FACTOR_MIL, distancia)

        cursor.execute(f'insert into disparo \
            (d_lato,d_lono,d_latd,d_lond,m_id,b_id,w_id,a_id,d_dist) \
            values \
            ({lat},{lon},{lati},{loni},{m_id},{b_id},{w_id},{a_id},{int(distancia)})')
        dbb.commit()
        cursor.close()
        dbb.close()  

        return "OK\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=15000, debug=False)

