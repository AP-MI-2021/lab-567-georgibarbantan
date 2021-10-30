from domain.vanzari2 import getTitlu, getNewSale, getId, getPret, getTipRedCl


def modifyGen(titlu, gen, lista):
    '''
    Modificarea genului unei carti cu un anumit titlu dat.
    :param lista: lista de vanzari
    :return: lista unde se modifica genul unei carti cu titlul dat
    '''

    lista_new = []

    for sale in lista:
        if getTitlu(sale) == titlu:
            newSale = getNewSale(
                getId(sale),
                getTitlu(sale),
                gen,
                getPret(sale),
                getTipRedCl(sale),
            )
            lista_new.append(newSale)
        else:
            lista_new.append(sale)

    return lista_new