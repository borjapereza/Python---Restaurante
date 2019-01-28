from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
import sqlite3
import locale

try:
    bbdd = 'dataBaseRestaurante'
    conexion = sqlite3.connect(bbdd)
    cur = conexion.cursor()
    print('BASE DE DATOS CONECTADA')

except sqlite3.OperationalError as e:
    print(e)


def cerrarConexion():
    try:
        conexion.commit()
        conexion.close()
        print('cerrando base de datos')
    except sqlite3.OperationalError as e:
        print(e)

def cabecera(cser):

    try:
        cser.setTitle('Informes')
        cser.setAuthor('Alfonso Fernández Álvarez')
        cser.setFont('Helvetica', 11)

        cser.line(50, 820, 525, 820)
        cser.line(50, 745, 525, 745)
        textnom = 'RESTAURANTE TEIS'
        textdir = 'Calle Maxwell S/N- Vigo'
        texttlfo = '555 55 55 55'
        cser.drawString(255, 795, textnom)
        cser.drawString(245, 775, textdir)
        cser.drawString(280, 755, texttlfo)
    except:
        print ('erros cabecera')

def pie(cser):
    try:
        cser.line(50, 20, 525, 20)
        textgracias = "Gracias por su visita"
        cser.drawString(270, 10, textgracias)

    except:
        print('erros pie')

def reportservicios():
    try:
        cser = canvas.Canvas('servicios.pdf', pagesize=A4)
        cabecera(cser)
        pie(cser)
        textlistado = 'LISTADO DE SERVICIOS'
        cser.drawString(255, 705, textlistado)
        cser.line(50,700,525,700)
        x = 50
        y = 680
        listado = servicios.mostrarservicios()
        for registro in listado:
            for i in range(3):
                cser.drawString(x,y,str(registro[i]))
                x = x + 220
            y = y -20
            x = 50
        cser.showPage()
        cser.save()
        dir = os.getcwd()
        os.system('/usr/bin/xdg-open ' + dir + '/servicios.pdf')

    except:
        print('error en informe')


def factura(idfactura):
    try:
        cser = canvas.Canvas( str(idfactura) + '.pdf', pagesize=A4)

        cabecera(cser)
        pie(cser)
        cur.execute('select c.idventa, s.servicio, c.cantidad, s.preciounidad from LineaFactura as c inner join servicio as s on s.IdServicio = c.IdServicio  where c.idfactura = ?', (idfactura,))
        listado = cur.fetchall()
        conexion.commit()
        textlistado = 'Factura'
        cser.drawString(255, 705, textlistado)
        cser.line(50, 700, 525, 700)
        x = 50
        y = 680
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
        cser.drawString(x, y, 'Total: ')
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
