from domain.vanzari import toString
from logic.CRUD import addSale, deleteSale, modifySale


def printMenu():
    print("1. Adaugare vanzare ")
    print("2. Stergere vanzare ")
    print("3. Modificare vanzare ")
    print("a. Afisare vanzare ")
    print("X. Iesire")


def uiAddSale(lista):
    id = input("Dati id-ul ")
    titlu = input("Dati titlul ")
    gen = input("Dati genul ")
    pret = float(input("Dati pretul "))
    tip_red_cl = input("Dati tipul reducere client ")

    return addSale(id, titlu, gen, pret, tip_red_cl, lista)


def uiDeleteSale(lista):
    id = input("Dati id-ul vanzarii pe care vreti sa o stergeti ")
    return deleteSale(id,lista)


def uiModifySale(lista):
    id = input("Dati id-ul vanzarii de modificat ")
    titlu = input("Dati noul titlu ")
    gen = input("Dati noul gen ")
    pret = float(input("Dati noul pret "))
    tip_red_cl = input("Dati noul tip de reducere client ")
    return modifySale(id, titlu, gen, pret, tip_red_cl, lista)

def showAll(lista):
    for sale in lista:
        print(toString(sale))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune=="1":
            lista = uiAddSale(lista)
        elif optiune=="2":
            lista = uiDeleteSale(lista)
        elif optiune=="3":
            lista = uiModifySale(lista)
        elif optiune=="a":
            showAll(lista)
        elif optiune=="x":
            break
        else:
            print("Optiune invalida! Reincercati!")