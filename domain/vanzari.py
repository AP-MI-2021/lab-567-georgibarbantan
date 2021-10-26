
def getNewSale(_id: str, _titlu: str, _gen: str, _pret: float, _tip_red_cl: str):
    sale = {
        'id': _id,
        'titlu': _titlu,
        'gen': _gen,
        'pret': _pret,
        'tip_red_cl': _tip_red_cl
    }
    return sale

def getId(sale):
    '''
    Da id-ul unui obiect
    :param obiect: dictionar ce retine un obiect
    :return: id-ul obiectului
    '''
    return sale["id"]

def getTitlu(sale):
    '''
    Da numele unui obiect
    :param obiect: dictionar ce retine un obiect
    :return: numele obiectului
    '''
    return sale["titlu"]

def getGen(sale):
    '''
    Da descrierea unui obiect
    :param obiect: dictionar ce retine un obiect
    :return: descrierea obiectului
    '''
    return sale["gen"]

def getPret(sale):
    '''
    Da pretul unui obiect
    :param obiect: dictionar ce retine un obiect
    :return: pretul obiectului
    '''
    return sale["pret"]

def getTipRedCl(sale):
    '''
    Da locatia unui obiect
    :param obiect: dictionar ce retine un obiect
    :return: locatia obiectului
    '''
    return sale["tip_red_cl"]

def toString(sale):
    return "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Locatie: {}".format(
        getId(sale),
        getTitlu(sale),
        getGen(sale),
        getPret(sale),
        getTipRedCl(sale)
    )