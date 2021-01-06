#! /usr/bin/python3

def suma_koszyka(kosz):
    suma = 0
    il_wszyst_prod = 0
    nabial = 0
    kwota_nabial = 0
    for poz in kosz:
        c = poz['cena']
        il = poz['ilosc']
        n = poz['nazwa']
        il_wszyst_prod += il
        poz_cena = c * il
        suma = suma + poz_cena
        if n in ('ser', 'mleko', 'jogurt'):
            nabial +=il
            kwota_nabial = kwota_nabial+poz_cena
    print("Kwota bez rabatów : ", suma)
    #R1 rabat 10% na produkty z kategorii nabial
    if nabial >=5:
        print("Rabat 10% na nabial : 5 lub wiecej produktów z kategorii nabial.")
        suma -=kwota_nabial*10/100
    #R2 rabat 10% : kwota do zaplaty 50 zl lub wyzsza
    if suma >= 50:
        suma = suma*90/100
        print("Rabat 10 % : kwota do zapłaty równa 50 lub wyzsza.")
    #R3  rabat 5% : 5 lub wiecej prod. w koszyku
    elif il_wszyst_prod >= 5:
        suma = suma*95/100
        print("Rabat 5 % : wiecej niz 5 prod. w koszyku. Naliczono rabat 5%.")

    return round(suma, 2)

if __name__ == "__main__":
    koszyk1 = [
        {'nazwa' : 'banany', 'ilosc': 1, 'cena' : 2.50},
        {'nazwa' : 'ser','ilosc': 1, 'cena' : 3.20},
        {'nazwa' : 'sok','ilosc': 3, 'cena' : 5.00},
        {'nazwa' : 'szynka', 'ilosc': 1,'cena' : 4.50},
        {'nazwa' : 'czekolada','ilosc': 5, 'cena' : 4.20}
        ]
    #0rabatow
    koszyk2 = [
        {'nazwa' : 'szynka', 'ilosc': 1,'cena' : 4.50},
        {'nazwa' : 'czekolada','ilosc': 2, 'cena' : 4.20}
        ]
    #nabial, wiecej niz 5 p.
    koszyk3 = [
        {'nazwa' : 'jogurt', 'ilosc': 3, 'cena' : 1.50},
        {'nazwa' : 'ser','ilosc': 2, 'cena' : 3.20},
        {'nazwa' : 'czekolada','ilosc': 5, 'cena' : 4.20}
        ]
    #powyzej 50 zl
    koszyk4 = [
        {'nazwa' : 'banany', 'ilosc': 1, 'cena' : 2.50},
        {'nazwa' : 'ser','ilosc': 1, 'cena' : 3.20},
        {'nazwa' : 'wino','ilosc': 3, 'cena' : 25.00},
        {'nazwa' : 'szynka', 'ilosc': 4,'cena' : 4.50},
        {'nazwa' : 'czekolada','ilosc': 5, 'cena' : 4.20}
        ]
    #nabial, powyzej 50 zl
    koszyk5 = [
        {'nazwa' : 'mleko', 'ilosc': 2, 'cena' : 3.50},
        {'nazwa' : 'ser','ilosc': 3, 'cena' : 3.20},
        {'nazwa' : 'wino','ilosc': 2, 'cena' : 25.00},
        {'nazwa' : 'szynka', 'ilosc': 4,'cena' : 4.50},
        {'nazwa' : 'czekolada','ilosc': 5, 'cena' : 4.20}
        ]

print("Do zapłaty : ", suma_koszyka(koszyk1))
print("Do zapłaty : ", suma_koszyka(koszyk2))
print("Do zapłaty : ", suma_koszyka(koszyk3))
print("Do zapłaty : ", suma_koszyka(koszyk4))
print("Do zapłaty : ", suma_koszyka(koszyk5))
