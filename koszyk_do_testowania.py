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
    #R1 rabat 10% na produkty z kategorii nabial
    if nabial >=5:
        #print("Rabat 10% na nabial")
        suma -=kwota_nabial*10/100
    #R2 rabat 10% : kwota do zaplaty 50 zl lub wyzsza (R2 I R3 sie wykluczaja)
    if suma >= 50:
        suma = suma*90/100
        #print("Rabat 10 % na wszystkie produkty")
    #R3  rabat 5% : 5 lub wiecej prod. w koszyku
    elif il_wszyst_prod >= 5:
        suma = suma*95/100
        #print("Rabat 5 % na wszystkie produkty")

    return round(suma, 2)


koszyk = [
    {'nazwa' : 'banany', 'ilosc': 1, 'cena' : 2.50},
    {'nazwa' : 'ser','ilosc': 1, 'cena' : 3.20},
    {'nazwa' : 'sok','ilosc': 3, 'cena' : 5.00},
    {'nazwa' : 'szynka', 'ilosc': 1,'cena' : 4.50},
    {'nazwa' : 'czekolada','ilosc': 5, 'cena' : 4.20}
    ]

#print("Do zaplaty : ", suma_koszyka(koszyk))
