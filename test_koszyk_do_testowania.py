import unittest
from koszyk_do_testowania import suma_koszyka

class TestKoszyk(unittest.TestCase):

    def test_koszyka1(self): #R3 : wiecej niz 5 produktow
        koszyk1 = [
            {'nazwa' : 'banany', 'ilosc': 1, 'cena' : 2.50},
            {'nazwa' : 'ser','ilosc': 1, 'cena' : 3.20},
            {'nazwa' : 'sok','ilosc': 3, 'cena' : 5.00},
            {'nazwa' : 'szynka', 'ilosc': 1,'cena' : 4.50},
            {'nazwa' : 'czekolada','ilosc': 5, 'cena' : 4.20}
            ]
        suma = suma_koszyka(koszyk1)
        self.assertEqual(suma, 43.89)

    def test_koszyka2(self): #0rabatow
        koszyk2 = [
            {'nazwa' : 'szynka', 'ilosc': 1,'cena' : 4.50},
            {'nazwa' : 'czekolada','ilosc': 2, 'cena' : 4.20}
            ]
        suma = suma_koszyka(koszyk2)
        self.assertEqual(suma, 12.9)
    def test_koszyka3(self): #R1, R3 : nabial, wiecej niz 5 produktow
        koszyk3 = [
            {'nazwa' : 'jogurt', 'ilosc': 3, 'cena' : 1.50},
            {'nazwa' : 'ser','ilosc': 2, 'cena' : 3.20},
            {'nazwa' : 'czekolada','ilosc': 5, 'cena' : 4.20}
            ]
        suma = suma_koszyka(koszyk3)
        self.assertEqual(suma, 29.27)
    def test_koszyka4(self):  #R2 : powyzej 50 zl
        koszyk4 = [
            {'nazwa' : 'banany', 'ilosc': 1, 'cena' : 2.50},
            {'nazwa' : 'ser','ilosc': 1, 'cena' : 3.20},
            {'nazwa' : 'wino','ilosc': 3, 'cena' : 25.00},
            {'nazwa' : 'szynka', 'ilosc': 4,'cena' : 4.50},
            {'nazwa' : 'czekolada','ilosc': 5, 'cena' : 4.20}
            ]
        suma = suma_koszyka(koszyk4)
        self.assertEqual(suma, 107.73)
    def test_koszyka5(self): #R1, R2 : nabial, powyzej 50 zl
        koszyk5 = [
            {'nazwa' : 'mleko', 'ilosc': 2, 'cena' : 3.50},
            {'nazwa' : 'ser','ilosc': 3, 'cena' : 3.20},
            {'nazwa' : 'wino','ilosc': 2, 'cena' : 25.00},
            {'nazwa' : 'szynka', 'ilosc': 4,'cena' : 4.50},
            {'nazwa' : 'czekolada','ilosc': 5, 'cena' : 4.20}
            ]
        suma = suma_koszyka(koszyk5)
        self.assertEqual(suma, 93.55)
