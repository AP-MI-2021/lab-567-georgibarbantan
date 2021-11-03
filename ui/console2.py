from domain.vanzari2 import toString
from logic.CRUD import addSale, modifySale, deleteSale
from logic.functionality import reducere
from logic.functionality2 import modifyGen


def showAll(lista_sale):
    for sale in lista_sale:
        print(toString(sale))

def uiAddSale(list_command_details, lista_sale):
    try:
        id = input(list_command_details[1])
        titlu = input(list_command_details[2])
        gen = input(list_command_details[3])
        pret = float(input(list_command_details[4]))
        tip_red_cl = input(list_command_details[5])
        return addSale(id, titlu, gen, pret, tip_red_cl, lista_sale)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista_sale

def uiDeleteSale(list_command_details, lista_sale):
    try:
        id = input(list_command_details[1])
        return deleteSale(id,lista_sale)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista_sale


def uiModifySale(list_command_details, lista_sale):
    try:
        id = input(list_command_details[1])
        titlu = input(list_command_details[2])
        gen = input(list_command_details[3])
        pret = float(input(list_command_details[4]))
        tip_red_cl = input(list_command_details[5])
        return modifySale(id, titlu, gen, pret, tip_red_cl, lista_sale)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista_sale


def uiModifyGen(list_command_details, lista_sale):
    titlu = input(list_command_details[1])
    gen = input(list_command_details[2])
    return modifyGen(titlu, gen, lista_sale)

def uiReducere(list_command_details, lista_sale):
    return reducere(lista_sale)

def show_menu():
    print("""
    Adaugare vanzare: id_vanzare, titlu, gen, pret, tip_reducere_client
    Stergere vanzare: id_vanzare
    Modificare vanzare: id_vanzare, titlu, gen, pret, tip_reducere_client
    Modificare gen: titlu, gen
    Show all
    Iesire
     """)

def console_2(lista_sale):

    try:
        while True:
            show_menu()
            commands = input("Introduceti comenzile separate prin ';' si instructiunile comenzii separate prin ',' ")
            commands = commands.split(sep = ";")
            for command in commands:
                command = command.split(sep = ",")
            list_command_details = []
            for command_details in command:
                list_command_details.append(command_details)
            if list_command_details[0] == "Adaugare vanzare":
                lista_sale = uiAddSale(list_command_details, lista_sale)
            elif list_command_details[0] == "Stergere vanzare":
                lista_sale = uiDeleteSale(list_command_details, lista_sale)
            elif list_command_details[0] == "Modificare vanzare":
                lista_sale = uiModifySale(list_command_details, lista_sale)
            elif list_command_details[0] == "Modificare gen":
                lista_sale = uiModifyGen(list_command_details, lista_sale)
            elif list_command_details[0] == "Reducere":
                lista_sale = uiReducere(list_command_details, lista_sale)
            elif list_command_details[0] == "Show all":
                showAll(lista_sale)
            elif list_command_details[0] == "Iesire":
                break
            else:
                print("Comanda nu este valida! Reincercati! ")
    except Exception as ex:
        print("Eroare, reincercati!", ex)
