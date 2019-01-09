import os
import sqlite3
import Restaurante

try:
    bbdd = 'dataBaseRestaurante'
    conex = sqlite3.connect(bbdd)
    cur = conex.cursor()
    print('BASE DE DATOS CONECTADA')

except sqlite3.OperationalError as e:
    print(e)

def cerrarConexion():
    try:
        conex.commit()
        conex.close()
        print('cerrando base de datos')
    except sqlite3.OperationalError as e:
        print(e)

def altaMesa(mesa):
    try:
        cur.execute("INSERT INTO MESA(Idmesa,MaxComensales) values(?,?)", mesa)
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()

def cargaMesas (ListaMesas,treeMesas):
    try:
        ListaMesas.clear()
        cur.execute("SELECT * FROM Mesa")
        cursor = cur.fetchall()
        for row in cursor:
            CargaMesas(treeMesas, ListaMesas, row)
    except sqlite3.OperationalError as e:
        print(e)

def CargaMesas(treeMesas,ListaMesas,fila):
    ListaMesas.append(fila)
    treeMesas.show()