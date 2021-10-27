from domain.vanzari2 import getPret
from logic.CRUD import addSale, getById
from logic.functionality import reducere


def test_reducere():
    lista = []
    lista = addSale("1", "Alchimistul", "Fictiune", 40, "silver", lista)
    lista = addSale("2", "Moara cu noroc", "Nuvela psihologica", 30, "none", lista)
    lista = addSale("3", "Ion", "roman realist", 25, "gold", lista)
    lista = reducere(lista)

    assert getPret(getById("1", lista)) == 38
    assert getPret(getById("2", lista)) == 30
    assert getPret(getById("3", lista)) == 22.5