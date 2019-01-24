import sqlite3
import datetime

from gi.repository import Gtk

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


def cargaMesas(ListaMesas, treeMesas, mesa1, mesa2, mesa3, mesa4, mesa5, mesa6, mesa7, mesa8):
    try:
        ListaMesas.clear()
        cur.execute("SELECT * FROM Mesa")
        cursor = cur.fetchall()
        for row in cursor:
            if row[0] == 1:
                mesa1.set_sensitive(False);
            if row[0] == 2:
                mesa2.set_sensitive(False);
            if row[0] == 3:
                mesa3.set_sensitive(False);
            if row[0] == 4:
                mesa4.set_sensitive(False);
            if row[0] == 5:
                mesa5.set_sensitive(False);
            if row[0] == 6:
                mesa6.set_sensitive(False);
            if row[0] == 7:
                mesa7.set_sensitive(False);
            if row[0] == 8:
                mesa8.set_sensitive(False);
            CargaMesas(ListaMesas, treeMesas, row)
    except sqlite3.OperationalError as e:
        print(e)


def CargaMesas(ListaMesas, treeMesas, fila):
    ListaMesas.append(fila)
    treeMesas.show()


def cargaMesasInicio(ListaMesas, treeMesas, image1, image2, image3, image4, image5, image6, image7, image8, mesa1,
                     mesa2, mesa3, mesa4, mesa5, mesa6, mesa7, mesa8):
    try:
        ListaMesas.clear()
        image1.set_from_file("img/MesasIndividiales3.png");
        mesa1.set_sensitive(True)
        image2.set_from_file("img/MesasIndividiales3.png");
        mesa2.set_sensitive(True)
        image3.set_from_file("img/MesasIndividiales3.png");
        mesa3.set_sensitive(True)
        image4.set_from_file("img/MesasIndividiales3.png");
        mesa4.set_sensitive(True)
        image5.set_from_file("img/MesasIndividiales2.png");
        mesa5.set_sensitive(True)
        image6.set_from_file("img/MesasIndividiales2.png");
        mesa6.set_sensitive(True)
        image8.set_from_file("img/MesasIndividiales1.png");
        mesa7.set_sensitive(True)
        image7.set_from_file("img/MesasIndividiales1.png");
        mesa8.set_sensitive(True)

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
                image8.set_from_file("img/MesasIndividiales1Azul.png");
                mesa7.set_sensitive(False)
            if row[0] == 8:
                image7.set_from_file("img/MesasIndividiales1Azul.png");
                mesa8.set_sensitive(False)
            CargaMesas(ListaMesas, treeMesas, row)
    except sqlite3.OperationalError as e:
        print(e)


def vaciarMesa(idMesa):
    try:
        cur.execute("DELETE FROM Mesa "
                    "where (Idmesa=?)", (idMesa,))
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()


def comprobarUser(usuario, contraseña, ventana):
    try:
        cur.execute("SELECT * FROM Camarero")
        cursor = cur.fetchall()
        for row in cursor:

            if row[1] == usuario and row[2] == contraseña:
                ventana.hide()

    except sqlite3.OperationalError as e:
        print(e)


def añadirComida(NombPlato, PrecioPlato, ventana):
    fila = (NombPlato, PrecioPlato)

    try:
        cur.execute("SELECT * FROM Servicio")
        cursor = cur.fetchall()

        if cursor != []:
            for row in cursor:
                if row[1] == NombPlato:
                    ventana.hide()

            try:
                cur.execute("INSERT INTO Servicio(Servicio,Preciounidad) values(?,?)", fila)
                conex.commit()
                ventana.hide()
            except sqlite3.OperationalError as e:
                print(e)
                conex.rollback()
        else:
            try:
                cur.execute("INSERT INTO Servicio(Servicio,Preciounidad) values(?,?)", fila)
                conex.commit()
                ventana.hide()
            except sqlite3.OperationalError as e:
                print(e)
                conex.rollback()

    except sqlite3.OperationalError as e:
        print(e)


def CargarCMBComida(CMBComidas):
    i = 0
    cur.execute("SELECT * FROM Servicio")
    row = cur.fetchone()
    list = Gtk.ListStore(str)
    list.append([row[1]])
    all_rows = cur.fetchall()
    for row in all_rows:
        i = i + 1
        list.append([row[1]])

    for name in list:
        CMBComidas.append_text(name[0])

    conex.commit()


def crearFactura(mesa, usuario):
    try:
        cur.execute("SELECT * FROM Camarero")
        cursor = cur.fetchall()
        for row in cursor:

            if row[1] == usuario:
                id = row[0]

    except sqlite3.OperationalError as e:
        print(e)

    fila = (0, id, mesa[0], datetime.datetime.now(), "No")
    try:
        cur.execute("INSERT INTO FACTURA(DniCli,IdCamarero,Idmesa,fecha,pagada) values(?,?,?,?,?)", fila)
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()

def borrarFactura(idMesa):
    try:
        cur.execute("DELETE FROM FACTURA "
                    "where (Idmesa=?)", (idMesa,))
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()

def AñadirServicioFacturaLista(idmesa,nombreServicio,cantidad):
    try:
        cur.execute("SELECT * FROM FACTURA WHERE (Idmesa=?)",(idmesa,))
        cursor = cur.fetchall()
        for row in cursor:
            idfactu = row[0]

    except sqlite3.OperationalError as e:
        print(e)

    try:
        cur.execute("SELECT * FROM SERVICIO WHERE (Servicio=?)", (nombreServicio,))
        cursor = cur.fetchall()
        for row in cursor:
            idServicio = row[0]

    except sqlite3.OperationalError as e:
        print(e)

    cosas = (idfactu, idServicio, cantidad)
    try:
        cur.execute("INSERT INTO LINEAFACTURA(IdFactura,IdServicio,Cantidad) values(?,?,?)", cosas)
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()

def CargaServiciosMesa(ListaComandas,treeServicios,idMesa):
    try:
        ListaComandas.clear()
        cur.execute("SELECT LF.IdFactura,LF.IdServicio,S.Servicio,LF.Cantidad,S.Preciounidad FROM LINEAFACTURA as LF INNER JOIN Servicio as S ON LF.IdServicio=S.IdServicio INNER JOIN FACTURA AS F ON LF.IDFACTURA = F.IDFACTURA WHERE (F.Idmesa="+str(idMesa)+")")
        cursor = cur.fetchall()
        for row in cursor:
            CargarServicioLista(ListaComandas, treeServicios, row)
    except sqlite3.OperationalError as e:
        print(e)


def CargarServicioLista(ListaComandas, treeServicios, fila):
    ListaComandas.append(fila)
    treeServicios.show()

def borrarServicio(idServicio, idFactura):
    try:
        cur.execute("DELETE FROM LineaFactura "
                    "where (IdServicio=?) and (IdFactura=?)", (idServicio,idFactura))
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()

def CargarFacturasMesa(ListaFacturasMesa,treeFacturaMesa,idMesa):
    try:
        ListaFacturasMesa.clear()
        cur.execute("SELECT IDCamarero, IDFactura, fecha, Pagada from Factura where idmesa = "+str(idMesa)+";")
        cursor = cur.fetchall()
        for row in cursor:
            CargaFacturasMesa(ListaFacturasMesa, treeFacturaMesa, row)
    except sqlite3.OperationalError as e:
        print(e)

def CargaFacturasMesa(ListaFacturasMesa,treeFacturaMesa,fila):
    ListaFacturasMesa.append(fila)
    treeFacturaMesa.show()


def CargarClientes(listaClientes,treeclientes):
    try:
        listaClientes.clear()
        cur.execute("SELECT * from cliente")
        cursor = cur.fetchall()
        for row in cursor:
            CargaClientes(listaClientes, treeclientes, row)
    except sqlite3.OperationalError as e:
        print(e)


def CargaClientes(listaClientes, treeclientes, fila):
    listaClientes.append(fila)
    treeclientes.show()


def guardarCliente(dni, nombre, apellidos, direcc, provincia, ciudad):
    fila =dni,apellidos,nombre,direcc,provincia,ciudad
    try:
        cur.execute("INSERT INTO CLIENTE(DNI,APELLIDOS,NOMBRE,DIRECCION,PROVINCIA,CIUDAD) values(?,?,?,?,?,?)", fila)
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()


def BorrarCliente(dni):
    try:
        cur.execute("DELETE FROM CLIENTE "
                    "where (DNI=?)", (dni,))
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()


def AñadirClienteFactura(dni,idf):
    try:
        cur.execute("UPDATE FACTURA set DniCli='"+str(dni)+"',Pagada='Si' WHERE Pagada='No' AND IdFactura="+str(idf)+"")
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()