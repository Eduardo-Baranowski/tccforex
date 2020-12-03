from django.shortcuts import render
import MySQLdb
def cinco_periodos():
    con = MySQLdb.connect(host="localhost", user="root", passwd="********", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos")
    numrows = int(cursor.rowcount)
    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-5:
            lista.append(float(row[1]))
        elif cont > qt-5:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:5])) /5
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def dez_periodos():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-10:
            lista.append(float(row[1]))
        elif cont > qt-10:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:10])) / 10
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def vinte_periodos():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-20:
            lista.append(float(row[1]))
        elif cont > qt-20:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    ultimo = row[1]
    media = (sum(lista[0:20]))/20

    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cinquenta_periodos():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-50:
            lista.append(float(row[1]))
        elif cont > qt-50:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
        print(bid)
    ultimo = row[1]
    media = (sum(lista[0:50]))/50
    print(media)

    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cem_periodos():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-100:
            lista.append(float(row[1]))
        elif cont > qt-100:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:100]))/100
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def duzentos_periodos():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-200:
            lista.append(float(row[1]))
        elif cont > qt-200:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:200]))/200

    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'


def cinco_periodos15():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos15")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []

    for row in cursor.fetchall():

        if cont == qt-5:
            lista.append(float(row[1]))
        elif cont > qt-5:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:5]))/5
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'



def dez_periodos15():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos15")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-10:
            lista.append(float(row[1]))
        elif cont > qt-10:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:10]))/10
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def vinte_periodos15():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos15")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-20:
            lista.append(float(row[1]))
        elif cont > qt-20:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:20]))/20
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cinquenta_periodos15():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos15")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-50:
            lista.append(float(row[1]))
        elif cont > qt-50:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:50]))/50
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cem_periodos15():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos15")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-100:
            lista.append(float(row[1]))
        elif cont > qt-100:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:100]))/100
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def duzentos_periodos15():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos15")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-200:
            lista.append(float(row[1]))
        elif cont > qt-200:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:200]))/200
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cinco_periodos30():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos30")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []

    for row in cursor.fetchall():

        if cont == qt-5:
            lista.append(float(row[1]))
        elif cont > qt-5:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:5]))/5
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'



def dez_periodos30():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos30")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-10:
            lista.append(float(row[1]))
        elif cont > qt-10:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:10]))/10
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def vinte_periodos30():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos30")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-20:
            lista.append(float(row[1]))
        elif cont > qt-20:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:20]))/20
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cinquenta_periodos30():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos30")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-50:
            lista.append(float(row[1]))
        elif cont > qt-50:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:50]))/50
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cem_periodos30():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos30")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-100:
            lista.append(float(row[1]))
        elif cont > qt-100:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:100]))/100
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def duzentos_periodos30():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precos30")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-200:
            lista.append(float(row[1]))
        elif cont > qt-200:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:200]))/200
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cinco_periodosH1():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precosH1")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []

    for row in cursor.fetchall():

        if cont == qt-5:
            lista.append(float(row[1]))
        elif cont > qt-5:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:5]))/5
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'



def dez_periodosH1():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precosH1")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-10:
            lista.append(float(row[1]))
        elif cont > qt-10:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:10]))/10
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def vinte_periodosH1():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precosH1")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-20:
            lista.append(float(row[1]))
        elif cont > qt-20:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:20]))/20
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cinquenta_periodosH1():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precosH1")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-50:
            lista.append(float(row[1]))
        elif cont > qt-50:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
        print(bid)
    print('lista', lista[0:50])
    media = (sum(lista[0:50]))/50
    print(media)
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cem_periodosH1():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precosH1")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-100:
            lista.append(float(row[1]))
        elif cont > qt-100:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:100]))/100
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def duzentos_periodosH1():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precosH1")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-200:
            lista.append(float(row[1]))
        elif cont > qt-200:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:200]))/200
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'


def cinco_periodosD1():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precosD1")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []

    for row in cursor.fetchall():

        if cont == qt-5:
            lista.append(float(row[1]))
        elif cont > qt-5:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:5]))/5
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'



def dez_periodosD1():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precosD1")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-10:
            lista.append(float(row[1]))
        elif cont > qt-10:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:10]))/10
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def vinte_periodosD1():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precosD1")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-20:
            lista.append(float(row[1]))
        elif cont > qt-20:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:20]))/20
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cinquenta_periodosD1():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precosD1")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-50:
            lista.append(float(row[1]))
        elif cont > qt-50:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:50]))/50
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cem_periodosD1():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precosD1")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-100:
            lista.append(float(row[1]))
        elif cont > qt-100:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:100]))/100
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def duzentos_periodosD1():
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCCII")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCCII.precosD1")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-200:
            lista.append(float(row[1]))
        elif cont > qt-200:
            lista.append(float(row[1]))
        cont+=1
    cursor.execute("SELECT * FROM dbTCCII.bid")
    bid = 0
    for row in cursor.fetchall():
        bid = row[1]
    media = (sum(lista[0:200]))/200
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'


def home(request):

    smaCinco = cinco_periodos()
    smaDez = dez_periodos()
    smaVinte = vinte_periodos()
    smaCinquenta = cinquenta_periodos()
    smaCem = cem_periodos()
    smaDuzentos = duzentos_periodos()


    smaCinco15 = cinco_periodos15()
    smaDez15 = dez_periodos15()
    smaVinte15 = vinte_periodos15()
    smaCinquenta15 = cinquenta_periodos15()
    smaCem15 = cem_periodos15()
    smaDuzentos15 = duzentos_periodos15()

    smaCinco30 = cinco_periodos30()
    smaDez30 = dez_periodos30()
    smaVinte30 = vinte_periodos30()
    smaCinquenta30 = cinquenta_periodos30()
    smaCem30 = cem_periodos30()
    smaDuzentos30 = duzentos_periodos30()

    smaCincoH1 = cinco_periodosH1()
    smaDezH1 = dez_periodosH1()
    smaVinteH1 = vinte_periodosH1()
    smaCinquentaH1 = cinquenta_periodosH1()
    smaCemH1 = cem_periodosH1()
    smaDuzentosH1 = duzentos_periodosH1()

    smaCincoD1 = cinco_periodosD1()
    smaDezD1 = dez_periodosD1()
    smaVinteD1 = vinte_periodosD1()
    smaCinquentaD1 = cinquenta_periodosD1()
    smaCemD1 = cem_periodosD1()
    smaDuzentosD1 = duzentos_periodosD1()

    return render(request, 'home.html', context={'smaCinco':smaCinco, 'smaDez':smaDez, 'smaVinte':smaVinte, 'smaCinquenta':smaCinquenta, 'smaCem':smaCem, 'smaDuzentos':smaDuzentos, 'smaCinco15':smaCinco15, 'smaDez15':smaDez15, 'smaVinte15':smaVinte15, 'smaCinquenta15':smaCinquenta15, 'smaCem15':smaCem15, 'smaDuzentos15':smaDuzentos15, 'smaCinco30':smaCinco30, 'smaDez30':smaDez30, 'smaVinte30':smaVinte30, 'smaCinquenta30':smaCinquenta30, 'smaCem30':smaCem30, 'smaDuzentos30':smaDuzentos30, 'smaCincoH1':smaCincoH1, 'smaDezH1':smaDezH1, 'smaVinteH1':smaVinteH1, 'smaCinquentaH1':smaCinquentaH1, 'smaCemH1':smaCemH1, 'smaDuzentosH1':smaDuzentosH1, 'smaCincoD1':smaCincoD1, 'smaDezD1':smaDezD1, 'smaVinteD1':smaVinteD1, 'smaCinquentaD1':smaCinquentaD1, 'smaCemD1':smaCemD1, 'smaDuzentosD1':smaDuzentosD1})