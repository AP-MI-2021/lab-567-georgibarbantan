from domain.vanzari2 import getGen
from logic.CRUD import addSale, getById
from logic.functionality2 import modifyGen


def test_modifyGen():
    lista = []
    lista = addSale("1", "Alchimistul", "Fictiune", 40, "silver", lista)
    lista = addSale("2", "Moara cu noroc", "Nuvela psihologica", 30, "none", lista)
    lista = addSale("3", "Ion", "Roman psihologic", 25, "gold", lista)
    lista = modifyGen("Ion", "Roman realist", lista)
    lista = modifyGen("Moara cu noroc", "Nuvela de analiza", lista)

    assert getGen(getById("3", lista)) == "Roman realist"
    assert getGen(getById("2", lista)) == "Nuvela de analiza"