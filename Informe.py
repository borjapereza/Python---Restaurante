from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

import os
import sqlite3
import locale

"""
    # Accion que carga y registra las fuentes que va a usar los informes una vez generados
"""
pdfmetrics.registerFont(TTFont('MontserratTH', 'Montserrat-Thin.ttf'))
pdfmetrics.registerFont(TTFont('Montserrat', 'Montserrat-Regular.ttf'))
pdfmetrics.registerFont(TTFont('MontserratBL', 'Montserrat-Bold.ttf'))
pdfmetrics.registerFont(TTFont('MontserratAlt', 'MontserratAlternates-Regular.ttf'))

"""
    # Accion que conecta con la BBDD nada mas abrir el programa
"""
try:
    bbdd = 'dataBaseRestaurante'
    conexion = sqlite3.connect(bbdd)
    cur = conexion.cursor()
    print('BASE DE DATOS CONECTADA')

except sqlite3.OperationalError as e:
    print(e)


def cerrarConexion():
    """
        # Accion que cierra la bbdd una vez cierra el programa
    """
    try:
        conexion.commit()
        conexion.close()
        print('cerrando base de datos')
    except sqlite3.OperationalError as e:
        print(e)

def cabecera(cser):
    """
        # Accion dibuja la parte superior del informe
    """
    try:
        cser.setTitle('Informes')
        cser.setAuthor('Alfonso Fernández Álvarez')
        cser.setFont('Montserrat', 24)

        cser.line(50, 820, 525, 820)
        cser.line(50, 745, 525, 745)
        cser.line(50, 700, 525, 700)
        textnom = 'RealFooters Restaurant'
        textdir = 'Calle Maxwell S/N- Vigo'
        texttlfo = '555 55 55 55'
        cser.drawCentredString(297.5, 795, textnom)
        cser.setFont('MontserratTH', 11)
        cser.drawCentredString(297.5, 775, textdir)
        cser.drawCentredString(297.5, 755, texttlfo)
    except:
        print ('error cabecera')

def pie(cser):
    """
        # Accion que dibuja la parte del pie de informe
    """
    try:
        cser.line(50, 100, 525, 100)
        textgracias = "Gracias por su visita"
        cser.drawCentredString(297.5, 50, textgracias)

    except:
        print('error pie')

def cliente(cser,dni):
    """
        # Accion que dibuja la parte del cliente del informe
    """
    Ayuda = ["DNI: ", "Apellidos: ", "Nombre: ", "Direccion: ", "Provincia: ", "Municipio: "]
    cser.setFont('MontserratAlt', 11)
    try:
        cur.execute(
            'select * from cliente where dni=?', (dni,))
        listado = cur.fetchall()
        conexion.commit()
        x = 50
        y = 590
        for registro in listado:
            for i in range(6):
                y = y + 15
                cser.drawString(x, y, Ayuda[i] +" "+ str(registro[i]))

    except:
        print('error cliente')

def factura(idfactura,dni):
    """
        # Accion que dibuja las comandas de esa mesa así como su importe y su importe total
    """
    try:
        cser = canvas.Canvas( str(idfactura) + '.pdf', pagesize=A4)

        cabecera(cser)
        pie(cser)
        cliente(cser,dni)
        cur.execute('select c.idventa, s.servicio, c.cantidad, s.preciounidad from LineaFactura as c inner join servicio as s on s.IdServicio = c.IdServicio  where c.idfactura = ?', (idfactura,))
        listado = cur.fetchall()
        conexion.commit()
        cser.setFont('MontserratBL', 11)
        textlistado = 'Factura'
        textcliente = 'Cliente'
        cser.drawString(255, 590, textlistado)
        cser.drawString(255, 710, textcliente)
        cser.line(50, 580, 525, 580)
        cser.setFont('Montserrat', 11)
        x = 50
        y = 540
        total = 0
        for registro in listado:
            for i in range(4):
                if i <= 1:
                    cser.drawString(x, y, str(registro[i]))
                    x = x + 40
                else:
                    x = x + 120
                    cser.drawString(x, y, str(registro[i]))


                var1 = int(registro[2])
                var2 = registro[3]
                var2 = var2
                var2 = round(float(var2), 2)
                subtotal = var1*var2
            total = total + subtotal
            subtotal = locale.currency(subtotal)
            x = x + 120
            cser.drawString(x, y, str(subtotal))
            y = y - 20
            x = 50
        y = y -20
        cser.line(50, y, 525, y)
        y = y -20
        x = 400
        cser.setFont('MontserratBL', 11)
        cser.drawString(x, y, 'Total: ')
        cser.setFont('Montserrat', 11)
        x = 485
        total = round(float(total), 2)
        total = locale.currency(total)
        cser.drawString(x,y,str(total))
        cser.showPage()
        cser.save()
        dir = os.getcwd()
        os.system('/usr/bin/xdg-open ' + dir + '/' + str(idfactura) + '.pdf')


    except sqlite3.OperationalError as e:
        print(e)
        conexion.rollback()
        print('error en factura')
