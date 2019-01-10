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
            if row[0] == 1:
                Restaurante.CargarImagenesInicio(1);
            if row[0] == 2:
                Restaurante.CargarImagenesInicio(2);
            if row[0] == 3:
                Restaurante.CargarImagenesInicio(3);
            if row[0] == 4:
                Restaurante.CargarImagenesInicio(4);
            if row[0] == 5:
                Restaurante.CargarImagenesInicio(5);
            if row[0] == 6:
                Restaurante.CargarImagenesInicio(6);
            if row[0] == 7:
                Restaurante.CargarImagenesInicio(7);
            if row[0] == 8:
                Restaurante.CargarImagenesInicio(8);
            CargaMesas(ListaMesas, treeMesas, row)
    except sqlite3.OperationalError as e:
        print(e)

def CargaMesas(ListaMesas, treeMesas, fila):
    ListaMesas.append(fila)
    treeMesas.show()

def cargaMesasInicio(ListaMesas,treeMesas,image1,image2,image3,image4,image5,image6,image7,image8,mesa1,mesa2,mesa3,mesa4,mesa5,mesa6,mesa7,mesa8):
    try:
        ListaMesas.clear()
        cur.execute("SELECT * FROM Mesa")
        cursor = cur.fetchall()
        for row in cursor:
            if row[0] == 1:
                image1.set_from_file("img/MesasIndividiales3Azul.png");
                mesa1.set_sensitive(False)
            if row[0] == 2:
                image2.set_from_file("img/MesasIndividiales3Azul.png");
                mesa2.set_sensitive(False)
            if row[0] == 3:
                image3.set_from_file("img/MesasIndividiales3Azul.png");
                mesa3.set_sensitive(False)
            if row[0] == 4:
                image4.set_from_file("img/MesasIndividiales3Azul.png");
                mesa4.set_sensitive(False)
            if row[0] == 5:
                image5.set_from_file("img/MesasIndividiales2Azul.png");
                mesa5.set_sensitive(False)
            if row[0] == 6:
                image6.set_from_file("img/MesasIndividiales2Azul.png");
                mesa6.set_sensitive(False)
            if row[0] == 7:
                image7.set_from_file("img/MesasIndividiales1Azul.png");
                mesa7.set_sensitive(False)
            if row[0] == 8:
                image8.set_from_file("img/MesasIndividiales1Azul.png");
                mesa8.set_sensitive(False)
            CargaMesas(ListaMesas, treeMesas, row)
    except sqlite3.OperationalError as e:
        print(e)