#!/usr/bin/python3
# -*- coding: utf-8 -*-
#comprobacion de permiso de acceso a sistema

global dbb,form,usuario, clave, userpas, DB_NAME,DB_USER,DB_USER_PW,DB_HOST

exec(open('CONFIGURACION.ini').read())


print('Content-Type:text/html;charset=utf-8\r\n')
print('\r\n')

import uuid, cgitb, cgi, sys, os
cgitb.enable()
import pymysql
dbb = pymysql.connect(db=DB_NAME,user=DB_USER,passwd=DB_USER_PW,host=DB_HOST)
cursor = dbb.cursor()

form = cgi.FieldStorage()
usuario = form.getvalue('usuario')
clave = form.getvalue('clave')
userpas = f'<input type="hidden" name="usuario" value="{usuario}" id="usuario" >  <input type="hidden" name="clave" value="{clave}" id="clave" >'


print ("<html><head>")
print (f'<title> {format(SYS_NAME)} </title>')
print ("<link rel=\"stylesheet\" type=\"text/css\" href=\"style/style.css\" >")
print ('<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">')


print ('</head>')
print ("<body>")
print ("<center>")
print (f"<h3>Sistema {format(SYS_NAME)} V{VERSION} Usuario: {usuario}</h3>")
print ("<hr size=\"8px\" color=\"black\" >")

##################################################
def printd (s):
	if DEBUG: print (f'<h4><pre>{s}</pre></h4>')

def	AutoTakeBack():
	print('<script language="JavaScript" type="text/javascript"> setTimeout("window.history.go(-1)",500);</script>')


def decrip(pw):
	return pw	#desactivado por ahora

	import base64
	from Crypto.Cipher import AES
	# aca desenrroscar la clave
	seckey = b'2212592520200448'
	chipher = AES.new(seckey,AES.MODE_ECB)
	return chipher.decrypt(base64.b64decode(pw))

def Habilitado (usuario):
    # verifica que el usuario este habilitado
    q = f'select users_enable from users where users_nom = "{usuario}"'
    cursor.execute(q)
    r = cursor.fetchone()
    if r == None: return False
    else: 
        if r[0] == 1: return True
        else: return False

def Acceso (usuario, clave):

    if not Habilitado(usuario): return False
    # verifica calve de usaurio
    q = f"select users_pwd from users where users_nom = \'{usuario}\'"
    cursor.execute(q)
    r = cursor.fetchone()
    if r == None:
        return False
    else:
        if clave == decrip(r[0]):
            return True
        else:
            return False

def AccesoSes (usuario, clave):
    if not Habilitado(usuario): return False

    #verifica sesion de usuaio y garantiza acceso
    q = f"select ses_session from ses where ses_users_nom = \'{usuario}\'"
    cursor.execute(q)
    r = cursor.fetchone()
    if r == None:
        return False
    else:

        if str(clave) == str(r[0]):
            return True
        else:
            return False


def AccesoAdmin (usuario):
    if not Habilitado(usuario): return False

    #verifica permiso de administrador
    q = f"select users_cat from users where users_nom = \'{usuario}\'"
    cursor.execute(q)
    r = cursor.fetchone()
    if r == None:
        return False
    else:
        if r[0]!="U":
            return True
        else:
            return False

def AccesoSuAdmin (usuario):
    if not Habilitado(usuario): return False

    #verifica permiso de administrador
    q = f"select users_cat from users where users_nom = \'{usuario}\'"
    cursor.execute(q)
    r = cursor.fetchone()
    if r == None:
        return False
    else:
        if r[0]=="S":
            return True
        else:
            return False


def getIDfromTable(campo_id,tabla,campo_nombre,valor):
    q = f'select {campo_id} from {tabla} where {campo_nombre} = "{valor}"'
    cursor.execute(q)
    r = cursor.fetchone()
    if not r:
        return 0
    else:
        return int(r[0])

def ImprimeBajoMenu (VolverA):
	print ('</h4><center><hr>')
	print ('<form method="post" action="AyudaSys.py">')
	print (userpas)
	print ('<input type="submit" value="Ver AYUDA" />')
	print ("</form>")
	print (f'<form method="post" action="{VolverA}">')
	print (userpas)
	print ('<input type="submit" value=" <<< VOLVER" />')
	print ("<hr></form>")
