from logic.CRUD import addSale
from tests.testall import runAllTests
from ui.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = addSale("1", "Alchimistul", "Fictiune", 40, "silver",lista)
    lista = addSale("2", "Moara cu noroc", "Nuvela psihologica", 30, "none", lista)
    runMenu(lista)

main()