from domain.vanzari2 import getTipRedCl, getNewSale, getId, getTitlu, getGen, getPret


def reducere(lista):
    '''
        Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold.
        :param lista: lista de vanzari
        :return: lista in care se aplica un discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold
    '''

    lista_new = []

    for sale in lista:
        if getTipRedCl(sale) == 'silver':
            newSale = getNewSale(
                getId(sale),
                getTitlu(sale),
                getGen(sale),
                getPret(sale) - 5 / 100 * getPret(sale),
                getTipRedCl(sale),
            )
            lista_new.append(newSale)

        elif getTipRedCl(sale) == 'gold':
            newSale = getNewSale(
                getId(sale),
                getTitlu(sale),
                getGen(sale),
                getPret(sale) - 10 / 100 * getPret(sale),
                getTipRedCl(sale),
            )
            lista_new.append(newSale)
        else:
            lista_new.append(sale)
    return lista_new