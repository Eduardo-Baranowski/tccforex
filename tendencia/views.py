from django.shortcuts import render
import MySQLdb

def cinco_periodos(numrows):
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCC1")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCC1.precos")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []

    for row in cursor.fetchall():
        if cont == qt-5:
            lista.append(float(row[2]))
        elif cont > qt-5:
            lista.append(float(row[2]))
        cont+=1
    bid = str(row[5])
    ultimo = row[1]
    media = (lista[0]+lista[1]+lista[2]+lista[3]+lista[4])/5
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'



def dez_periodos(numrows):
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCC1")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCC1.precos")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-10:
            lista.append(float(row[2]))
        elif cont > qt-10:
            lista.append(float(row[2]))
        cont+=1
    bid = str(row[5])
    ultimo = row[1]
    media = (lista[0]+lista[1]+lista[2]+lista[3]+lista[4]+lista[5]+lista[6]+lista[7]+lista[8]+lista[9])/10
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def vinte_periodos(numrows):
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCC1")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCC1.precos")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-20:
            lista.append(float(row[2]))
        elif cont > qt-20:
            lista.append(float(row[2]))
        cont+=1
    bid = str(row[5])
    ultimo = row[1]
    media = (sum(lista[0:19]))/20
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cinquenta_periodos(numrows):
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCC1")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCC1.precos")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-50:
            lista.append(float(row[2]))
        elif cont > qt-50:
            lista.append(float(row[2]))
        cont+=1
    bid = str(row[5])
    ultimo = row[1]
    media = (sum(lista[0:49]))/50
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def cem_periodos(numrows):
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCC1")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCC1.precos")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-100:
            lista.append(float(row[2]))
        elif cont > qt-100:
            lista.append(float(row[2]))
        cont+=1
    bid = str(row[5])
    ultimo = row[1]
    media = (sum(lista[0:99]))/100
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def duzentos_periodos(numrows):
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCC1")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCC1.precos")
    numrows = int(cursor.rowcount)

    qt = numrows
    cont = 0
    lista = []
    for row in cursor.fetchall():
        if cont == qt-200:
            lista.append(float(row[2]))
        elif cont > qt-200:
            lista.append(float(row[2]))
        cont+=1
    bid = str(row[5])
    ultimo = row[1]
    media = (sum(lista[0:199]))/200
    if float(bid) < media:
        return 'Venda'
    elif float(bid) > media:
        return 'Compra'

def home(request):
    con = MySQLdb.connect(host="localhost", user="root", passwd="Baranowski25", db="dbTCC1")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dbTCC1.precos")
    numrows = int(cursor.rowcount)

    smaCinco = cinco_periodos(numrows)
    smaDez = dez_periodos(numrows)
    smaVinte = vinte_periodos(numrows)
    smaCinquenta = cinquenta_periodos(numrows)
    smaCem = cem_periodos(numrows)
    smaDuzentos = duzentos_periodos(numrows)
    return render(request, 'home.html', context={'smaCinco':smaCinco, 'smaDez':smaDez, 'smaVinte':smaVinte, 'smaCinquenta':smaCinquenta, 'smaCem':smaCem, 'smaDuzentos':smaDuzentos})