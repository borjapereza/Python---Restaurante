# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Restaurante:

    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('Restaurante.glade')

        # Objetos
        self.venprincipal = b.get_object('VentanaPrincipal')

        # Diccionario
        # Eventos
        dic = {'on_VentanaPrincipal_destroy': self.btnsal,
               }

        self.venprincipal.show()

    def btnsal(self, data=None):
        Gtk.main_quit()

if __name__ == '__main__':
    main = Restaurante()
    Gtk.main()
