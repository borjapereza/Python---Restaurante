# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import gi
import BBDD
import BBDD2

gi.require_version('Gtk', '3.0')
from gi.repository import Gdk, Gtk
from os.path import abspath, dirname, join

WHERE_AM_I = abspath(dirname(__file__))


class Restaurante:

    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('Restaurante.glade')

        # Cargar el aspecto de la  app
        self.set_style()

        # Objetos Ventana Mesas
        self.venprincipal = b.get_object('VentanaPrincipal')
        self.WinLogCamarero = b.get_object('WinLogCamarero')
        self.WinAñadirComidas = b.get_object('WinAñadirComidas')
        self.BTNMesa1 = b.get_object('BTNMesa1')
        self.image1 = b.get_object('image1')
        self.BTNMesa2 = b.get_object('BTNMesa2')
        self.image2 = b.get_object('image2')
        self.BTNMesa3 = b.get_object('BTNMesa3')
        self.image3 = b.get_object('image3')
        self.BTNMesa4 = b.get_object('BTNMesa4')
        self.image4 = b.get_object('image4')
        self.BTNMesa5 = b.get_object('BTNMesa5')
        self.image5 = b.get_object('image5')
        self.BTNMesa6 = b.get_object('BTNMesa6')
        self.image6 = b.get_object('image6')
        self.BTNMesa7 = b.get_object('BTNMesa7')
        self.image7 = b.get_object('image7')
        self.BTNMesa8 = b.get_object('BTNMesa8')
        self.image8 = b.get_object('image8')
        self.CMBMesas = b.get_object('CMBMesas')
        self.BTNOcuparMesa = b.get_object('BTNOcuparMesa')
        self.BTNRealizarPago = b.get_object('BTNRealizarPago')
        self.BTNVaciarMesa = b.get_object('BTNVaciarMesa')
        self.treeMesas = b.get_object('treeMesas')
        self.ListaMesas = b.get_object('ListaMesas')
        self.CMBMesasServicios = b.get_object('CMBMesasServicios')
        self.lblNumeroComensales = b.get_object('lblNumeroComensales')
        self.BTNNuevasComandas = b.get_object('BTNNuevasComandas')
        self.BTNAñadirComanda = b.get_object('BTNAñadirComanda')
        self.BTNCancelarComanda = b.get_object('BTNCancelarComanda')
        self.BTNRealizarFactura = b.get_object('BTNRealizarFactura')
        self.etPass = b.get_object('etPass')
        self.etUser = b.get_object('etUser')
        self.BTNAñadir = b.get_object('BTNAñadir')
        self.BTNSalirAñadir = b.get_object('BTNSalirAñadir')
        self.etNombrePlato = b.get_object('etNombrePlato')
        self.etPrecioPlato = b.get_object('etPrecioPlato')
        self.CMBComidas = b.get_object('CMBComidas')
        self.etCantidadComida = b.get_object('etCantidadComida')
        self.ListaComandas = b.get_object('ListaComandas')
        self.treeServicios = b.get_object('treeServicios')
        self.CMBMesaFactura = b.get_object('CMBMesaFactura')
        self.treeClientes = b.get_object('treeClientes')
        self.treeFactuMesas = b.get_object('treeFactuMesas')
        self.listClientes = b.get_object('listClientes')
        self.listFactuMesa = b.get_object('listFactuMesa')
        self.WinAñadirCliente = b.get_object('WinAñadirCliente')
        self.cmbProvincia = b.get_object('cmbProvincia')
        self.cmbCiudad = b.get_object('cmbCiudad')
        self.edDNI = b.get_object('edDNI')
        self.edNombre = b.get_object('edNombre')
        self.edApellidos = b.get_object('edApellidos')
        self.edDireccion = b.get_object('edDireccion')

        # Diccionario
        # Eventos
        dic = {'on_VentanaPrincipal_destroy': self.btnsal,
               'on_BTNMesa1_clicked': self.clickMesa1,
               'on_BTNMesa2_clicked': self.clickMesa2,
               'on_BTNMesa3_clicked': self.clickMesa3,
               'on_BTNMesa4_clicked': self.clickMesa4,
               'on_BTNMesa5_clicked': self.clickMesa5,
               'on_BTNMesa6_clicked': self.clickMesa6,
               'on_BTNMesa7_clicked': self.clickMesa7,
               'on_BTNMesa8_clicked': self.clickMesa8,
               'on_BTNOcuparMesa_clicked': self.OcuparMesa,
               'on_treeMesas_cursor_changed': self.SeleccionarMesa,
               'on_BTNVaciarMesa_clicked': self.VaciarMesa,
               'on_WinLogCamarero_destroy': self.btnsal,
               'on_BTNSalirLog_clicked': self.btnsal,
               'on_BTNEnterLog_clicked': self.btnLog,
               'on_WinAñadirComidas_destroy': self.btnSalirAñadir,
               'on_BTNSalirAñadir_clicked': self.btnSalirAñadir,
               'on_BTNNuevasComandas_clicked': self.WinAñadirComida,
               'on_BTNAñadir_clicked': self.ADDComida,
               'on_BTNAñadirComanda_clicked': self.on_BTNAñadirComanda_clicked,
               'on_BTNCancelarComanda_clicked': self.on_BTNCancelarComanda_clicked,
               'on_BTNRealizarFactura_clicked': self.on_BTNRealizarFactura_clicked,
               'on_WinAñadirCliente_destroy': self.onSalirAñadirCliente,
               'on_btnAñadirCliente_clicked': self.ventanaAñadirCLiente,
               'on_btnCancelarCliente_clicked': self.onSalirAñadirCliente,
               'on_cmbProvincia_changed':self.on_cmbProvincia_changed,
               'on_btnAgregarCliente_clicked':self.on_btnAgregarCliente_clicked,
               'on_btnModificarCliente_clicked':self.on_btnModificarCliente_clicked,
               }

        b.connect_signals(dic)
        self.CMBMesas.set_sensitive(False)
        BBDD.cargaMesasInicio(self.ListaMesas, self.treeMesas, self.image1, self.image2, self.image3, self.image4,
                              self.image5, self.image6, self.image7, self.image8, self.BTNMesa1, self.BTNMesa2,
                              self.BTNMesa3, self.BTNMesa4, self.BTNMesa5, self.BTNMesa6, self.BTNMesa7,
                              self.BTNMesa8)
        BBDD.CargarCMBComida(self.CMBComidas)
        BBDD2.CargarProvincias(self.cmbProvincia)
        self.cmbCiudad.set_sensitive(False)
        BBDD.CargarClientes(self.listClientes, self.treeClientes)
        self.venprincipal.show()
        self.WinLogCamarero.show()

        # Cargamos el tema oscuro para nuestra app

    def set_style(self):
        provider = Gtk.CssProvider()
        provider.load_from_path(join(WHERE_AM_I, 'gtk-dark.css'))
        screen = Gdk.Display.get_default_screen(Gdk.Display.get_default())
        GTK_STYLE_PROVIDER_PRIORITY_APPLICATION = 600
        Gtk.StyleContext.add_provider_for_screen(
            screen, provider,
            GTK_STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def btnsal(self, data=None):
        Gtk.main_quit()

    def btnLog(self, data=None):
        BBDD.comprobarUser(self.etUser.get_text(), self.etPass.get_text(), self.WinLogCamarero)
        self.nombreCamarero = self.etUser.get_text()

    def btnSalirAñadir(self, data=None):
        self.WinAñadirComidas.hide()

    def WinAñadirComida(self, data=None):
        self.WinAñadirComidas.show()

    def ventanaAñadirCLiente(self, data=None):
        self.WinAñadirCliente.show()

    def onSalirAñadirCliente(self, data=None):
        self.WinAñadirCliente.hide()

    def ADDComida(self, data=None):
        BBDD.añadirComida(self.etNombrePlato.get_text(), self.etPrecioPlato.get_text(), self.WinAñadirComidas)
        self.CMBComidas.remove_all()
        BBDD.CargarCMBComida(self.CMBComidas)
        self.etNombrePlato.set_text("")
        self.etPrecioPlato.set_text("")

    def clickMesa1(self, witget, data=None):
        self.BTNOcuparMesa.set_sensitive(True)
        self.BTNRealizarPago.set_sensitive(False)
        self.BTNVaciarMesa.set_sensitive(False)
        self.CMBMesas.set_active(1)

    def clickMesa2(self, witget, data=None):
        self.BTNOcuparMesa.set_sensitive(True)
        self.BTNRealizarPago.set_sensitive(False)
        self.BTNVaciarMesa.set_sensitive(False)
        self.CMBMesas.set_active(2)

    def clickMesa3(self, witget, data=None):
        self.BTNOcuparMesa.set_sensitive(True)
        self.BTNRealizarPago.set_sensitive(False)
        self.BTNVaciarMesa.set_sensitive(False)
        self.CMBMesas.set_active(3)

    def clickMesa4(self, witget, data=None):
        self.BTNOcuparMesa.set_sensitive(True)
        self.BTNRealizarPago.set_sensitive(False)
        self.BTNVaciarMesa.set_sensitive(False)
        self.CMBMesas.set_active(4)

    def clickMesa5(self, witget, data=None):
        self.BTNOcuparMesa.set_sensitive(True)
        self.BTNRealizarPago.set_sensitive(False)
        self.BTNVaciarMesa.set_sensitive(False)
        self.CMBMesas.set_active(5)

    def clickMesa6(self, witget, data=None):
        self.BTNOcuparMesa.set_sensitive(True)
        self.BTNRealizarPago.set_sensitive(False)
        self.BTNVaciarMesa.set_sensitive(False)
        self.CMBMesas.set_active(6)

    def clickMesa7(self, witget, data=None):
        self.BTNOcuparMesa.set_sensitive(True)
        self.BTNRealizarPago.set_sensitive(False)
        self.BTNVaciarMesa.set_sensitive(False)
        self.CMBMesas.set_active(7)

    def clickMesa8(self, witget, data=None):
        self.BTNOcuparMesa.set_sensitive(True)
        self.BTNRealizarPago.set_sensitive(False)
        self.BTNVaciarMesa.set_sensitive(False)
        self.CMBMesas.set_active(8)

    def OcuparMesa(self, witget, data=None):
        if self.CMBMesas.get_active_text() == "Escoge una mesa":
            print("ERROR: Selecciona una Mesa")
        else:
            if self.CMBMesas.get_active_text() == "Mesa 1 (4 Personas)":
                self.image1.set_from_file("img/MesasIndividiales3Azul.png")
                self.CMBMesas.set_active(1)
                mesa = (1, 4)
                BBDD.altaMesa(mesa)
                BBDD.crearFactura(mesa, self.nombreCamarero)

            if self.CMBMesas.get_active_text() == "Mesa 2 (4 Personas)":
                self.image2.set_from_file("img/MesasIndividiales3Azul.png")
                self.CMBMesas.set_active(2)
                mesa = (2, 4)
                BBDD.altaMesa(mesa)
                BBDD.crearFactura(mesa, self.nombreCamarero)

            if self.CMBMesas.get_active_text() == "Mesa 3 (4 Personas)":
                self.image3.set_from_file("img/MesasIndividiales3Azul.png")
                self.CMBMesas.set_active(3)
                mesa = (3, 4)
                BBDD.altaMesa(mesa)
                BBDD.crearFactura(mesa, self.nombreCamarero)

            if self.CMBMesas.get_active_text() == "Mesa 4 (4 Personas)":
                self.image4.set_from_file("img/MesasIndividiales3Azul.png")
                self.CMBMesas.set_active(4)
                mesa = (4, 4)
                BBDD.altaMesa(mesa)
                BBDD.crearFactura(mesa, self.nombreCamarero)

            if self.CMBMesas.get_active_text() == "Mesa 5 (8 Personas)":
                self.image5.set_from_file("img/MesasIndividiales2Azul.png")
                self.CMBMesas.set_active(5)
                mesa = (5, 8)
                BBDD.altaMesa(mesa)
                BBDD.crearFactura(mesa, self.nombreCamarero)

            if self.CMBMesas.get_active_text() == "Mesa 6 (8 Personas)":
                self.image6.set_from_file("img/MesasIndividiales2Azul.png")
                self.CMBMesas.set_active(6)
                mesa = (6, 8)
                BBDD.altaMesa(mesa)
                BBDD.crearFactura(mesa, self.nombreCamarero)

            if self.CMBMesas.get_active_text() == "Mesa 7 (10 Personas)":
                self.image8.set_from_file("img/MesasIndividiales1Azul.png")
                self.CMBMesas.set_active(7)
                mesa = (7, 10)
                BBDD.altaMesa(mesa)
                BBDD.crearFactura(mesa, self.nombreCamarero)

            if self.CMBMesas.get_active_text() == "Mesa 8 (10 Personas)":
                self.image7.set_from_file("img/MesasIndividiales1Azul.png")
                self.CMBMesas.set_active(8)
                mesa = (8, 10)
                BBDD.altaMesa(mesa)
                BBDD.crearFactura(mesa, self.nombreCamarero)

            BBDD.cargaMesas(self.ListaMesas, self.treeMesas, self.BTNMesa1, self.BTNMesa2,
                            self.BTNMesa3, self.BTNMesa4, self.BTNMesa5, self.BTNMesa6, self.BTNMesa7,
                            self.BTNMesa8)

    def SeleccionarMesa(self, witget, data=None):
        model, iter = self.treeMesas.get_selection().get_selected()

        if iter != None:
            idMesa = model.get_value(iter, 0)
            numeroPersonas = model.get_value(iter, 1)
            self.CMBMesas.set_active(idMesa)
            self.CMBMesasServicios.set_active(idMesa)
            self.CMBMesaFactura.set_active(idMesa)
            self.lblNumeroComensales.set_text(str(numeroPersonas))
            BBDD.CargaServiciosMesa(self.ListaComandas, self.treeServicios, idMesa)
            BBDD.CargarFacturasMesa(self.listFactuMesa, self.treeFactuMesas, idMesa)
            self.BTNOcuparMesa.set_sensitive(False)
            self.BTNRealizarPago.set_sensitive(True)
            self.BTNVaciarMesa.set_sensitive(True)

    def VaciarMesa(self, witget, data=None):
        model, iter = self.treeMesas.get_selection().get_selected()

        idMesa = model.get_value(iter, 0)
        BBDD.borrarFactura(idMesa)
        BBDD.vaciarMesa(idMesa)
        BBDD.cargaMesasInicio(self.ListaMesas, self.treeMesas, self.image1, self.image2, self.image3, self.image4,
                              self.image5, self.image6, self.image7, self.image8, self.BTNMesa1, self.BTNMesa2,
                              self.BTNMesa3, self.BTNMesa4, self.BTNMesa5, self.BTNMesa6, self.BTNMesa7,
                              self.BTNMesa8)

    def on_BTNAñadirComanda_clicked(self, witget, data=None):

        idmesa = self.CMBMesasServicios.get_active()
        nombreServicio = self.CMBComidas.get_active_text()
        cantidad = self.etCantidadComida.get_text()
        nombreMesa = self.CMBMesasServicios.get_active_text()
        if nombreMesa == "Mesa 1":
            idMesa = 1
        if nombreMesa == "Mesa 2":
            idMesa = 2
        if nombreMesa == "Mesa 3":
            idMesa = 3
        if nombreMesa == "Mesa 4":
            idMesa = 4
        if nombreMesa == "Mesa 5":
            idMesa = 5
        if nombreMesa == "Mesa 6":
            idMesa = 6
        if nombreMesa == "Mesa 7":
            idMesa = 7
        if nombreMesa == "Mesa 8":
            idMesa = 8

        if cantidad == "":
            print("NO HAY NADA")
        else:
            BBDD.AñadirServicioFacturaLista(idmesa, nombreServicio, cantidad)
            self.etCantidadComida.set_text("")
            BBDD.CargaServiciosMesa(self.ListaComandas, self.treeServicios, idMesa)

    def on_BTNCancelarComanda_clicked(self, witget, data=None):
        model, iter = self.treeServicios.get_selection().get_selected()

        idFactura = model.get_value(iter, 0)
        idServicio = model.get_value(iter, 1)
        nombreMesa = self.CMBMesasServicios.get_active_text()
        if nombreMesa == "Mesa 1":
            idMesa = 1
        if nombreMesa == "Mesa 2":
            idMesa = 2
        if nombreMesa == "Mesa 3":
            idMesa = 3
        if nombreMesa == "Mesa 4":
            idMesa = 4
        if nombreMesa == "Mesa 5":
            idMesa = 5
        if nombreMesa == "Mesa 6":
            idMesa = 6
        if nombreMesa == "Mesa 7":
            idMesa = 7
        if nombreMesa == "Mesa 8":
            idMesa = 8

        BBDD.borrarServicio(idServicio, idFactura)
        BBDD.CargaServiciosMesa(self.ListaComandas, self.treeServicios, idMesa)

    def on_BTNRealizarFactura_clicked(self, witget, data=None):
        print(20)

    def on_cmbProvincia_changed(self, witget, data=None):
        self.cmbCiudad.remove_all()
        nombre = self.cmbProvincia.get_active_text()
        BBDD2.CargarMunicipios(self.cmbCiudad,nombre)

    def on_btnAgregarCliente_clicked(self, witget, data=None):
        nombre = self.edNombre.get_text()
        apellidos = self.edApellidos.get_text()
        direcc = self.edDireccion.get_text()
        dni = self.edDNI.get_text()
        ciudad = self.cmbCiudad.get_active_text()
        provincia = self.cmbProvincia.get_active_text()

        valido = self.validoDNI(dni)
        if valido:
            BBDD.guardarCliente(dni,nombre,apellidos,direcc,provincia,ciudad)
            BBDD.CargarClientes(self.listClientes,self.treeClientes)
            self.edNombre.set_text("")
            self.edApellidos.set_text("")
            self.edDireccion.set_text("")
            self.edDNI.set_text("")
            self.cmbCiudad.remove_all()
            self.WinAñadirCliente.hide()
        else:
            print("DNI NO VALIDO")

    def validoDNI(self, dni):

        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
        numeros = "1234567890"
        dni = str(dni).upper()
        # dni="12345678Z"
        if len(dni) == 9:
            dig_control = dni[8]
            dni = dni[:8]
            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
        return False

    def on_btnModificarCliente_clicked(self, witget, data=None):
        model, iter = self.treeClientes.get_selection().get_selected()

        dni = model.get_value(iter, 0)
        BBDD.BorrarCliente(dni)
        BBDD.CargarClientes(self.listClientes, self.treeClientes)

if __name__ == '__main__':
    main = Restaurante()
    Gtk.main()
