from domain.vanzari import getNewSale, getId


def addSale(id, titlu, gen, pret, tip_red_cl, lista):
    '''
    Adauga un obiect intr-o lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: o lista continand vechile obiecte si noul obiect
    '''
    sale = getNewSale(id, titlu, gen, pret, tip_red_cl)
    return lista + [sale]

def getById(id, lista):
    '''
    Da elementul din lista cu un id dat
    :param id: string
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat sau None daca nu exista
    '''
    for sale in lista:
        if getId(sale) == id:
            return sale
    return None

def deleteSale(id, lista):
    '''
    Sterge obiectul cu id-ul dat dintr-o lista
    :param id: id-ul obiectului care se va sterge
    :param lista: lista de obiecte
    :return: o lista de obiecte fara obiectul cu id-ul dat
    '''

    return [sale for sale in lista if getId(sale)!= id]

def modifySale(id, titlu, gen, pret, tip_red_cl, lista):
    '''
    Modifica obiectul cu id-ul dat
    :param id: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret: pretul obiectului
    :param locatie: locatia obiectului
    :param lista: o lista de obiecte
    :return: lista modificata
    '''
    listaNoua=[]
    for sale in lista:
        if getId(sale)==id:
            newSale = getNewSale(id, titlu, gen, pret, tip_red_cl)
            listaNoua.append(newSale)
        else:
            listaNoua.append(sale)
    return listaNoua