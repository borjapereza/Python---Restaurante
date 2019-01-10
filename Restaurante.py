# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import gi
import BBDD

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Restaurante:

    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('Restaurante.glade')

        # Objetos Ventana Mesas
        self.venprincipal = b.get_object('VentanaPrincipal')
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
               }

        b.connect_signals(dic)
        self.CMBMesas.set_sensitive(False)
        BBDD.cargaMesasInicio(self.ListaMesas, self.treeMesas, self.image1, self.image2, self.image3, self.image4,
                              self.image5, self.image6, self.image7, self.image8, self.BTNMesa1, self.BTNMesa2,
                              self.BTNMesa3, self.BTNMesa4, self.BTNMesa5, self.BTNMesa6, self.BTNMesa7,
                              self.BTNMesa8)
        self.venprincipal.show()

    def btnsal(self, data=None):
        Gtk.main_quit()

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
                self.image1.set_from_file("img/MesasIndividiales3Azul.png");
                self.CMBMesas.set_active(1)
                mesa = (1, 4)
                BBDD.altaMesa(mesa)
                BBDD.cargaMesas(self.ListaMesas, self.treeMesas)

            if self.CMBMesas.get_active_text() == "Mesa 2 (4 Personas)":
                self.image2.set_from_file("img/MesasIndividiales3Azul.png");
                self.CMBMesas.set_active(2)
                mesa = (2, 4)
                BBDD.altaMesa(mesa)
                BBDD.cargaMesas(self.ListaMesas, self.treeMesas)

            if self.CMBMesas.get_active_text() == "Mesa 3 (4 Personas)":
                self.image3.set_from_file("img/MesasIndividiales3Azul.png");
                self.CMBMesas.set_active(3)
                mesa = (3, 4)
                BBDD.altaMesa(mesa)
                BBDD.cargaMesas(self.ListaMesas, self.treeMesas)

            if self.CMBMesas.get_active_text() == "Mesa 4 (4 Personas)":
                self.image4.set_from_file("img/MesasIndividiales3Azul.png");
                self.CMBMesas.set_active(4)
                mesa = (4, 4)
                BBDD.altaMesa(mesa)
                BBDD.cargaMesas(self.ListaMesas, self.treeMesas)

            if self.CMBMesas.get_active_text() == "Mesa 5 (8 Personas)":
                self.image5.set_from_file("img/MesasIndividiales2Azul.png");
                self.CMBMesas.set_active(5)
                mesa = (5, 8)
                BBDD.altaMesa(mesa)
                BBDD.cargaMesas(self.ListaMesas, self.treeMesas)

            if self.CMBMesas.get_active_text() == "Mesa 6 (8 Personas)":
                self.image6.set_from_file("img/MesasIndividiales2Azul.png");
                self.CMBMesas.set_active(6)
                mesa = (6, 8)
                BBDD.altaMesa(mesa)
                BBDD.cargaMesas(self.ListaMesas, self.treeMesas)

            if self.CMBMesas.get_active_text() == "Mesa 7 (10 Personas)":
                self.image8.set_from_file("img/MesasIndividiales1Azul.png");
                self.CMBMesas.set_active(7)
                mesa = (7, 10)
                BBDD.altaMesa(mesa)
                BBDD.cargaMesas(self.ListaMesas, self.treeMesas)

            if self.CMBMesas.get_active_text() == "Mesa 8 (10 Personas)":
                self.image7.set_from_file("img/MesasIndividiales1Azul.png");
                self.CMBMesas.set_active(8)
                mesa = (8, 10)
                BBDD.altaMesa(mesa)
                BBDD.cargaMesas(self.ListaMesas, self.treeMesas)

    def SeleccionarMesa(self, witget, data=None):
        model, iter = self.treeMesas.get_selection().get_selected()

        if iter != None:
            idMesa = model.get_value(iter, 0)
            self.CMBMesas.set_active(idMesa)
            self.BTNOcuparMesa.set_sensitive(False)
            self.BTNRealizarPago.set_sensitive(True)
            self.BTNVaciarMesa.set_sensitive(True)

    def VaciarMesa(self, witget, data=None):
        mesa = (8, 10)

if __name__ == '__main__':
    main = Restaurante()
    Gtk.main()
