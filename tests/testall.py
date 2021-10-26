from tests.testCRUD import test_addSale, test_deleteSale, test_modifySale
from tests.testdomain import test_sale
from tests.testfunctionality import test_reducere


def runAllTests():
    test_sale()
    test_addSale()
    test_deleteSale()
    test_modifySale()
    test_reducere()