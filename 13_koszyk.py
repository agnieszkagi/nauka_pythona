#! /usr/bin/python3

#R1 rabat nabial 10%
def rabat_nabial(cena):
    print("(naliczono 10% rabatu na nabial)")
    return round(cena*9/10, 2)

#R2 rabat 5 produktów 5%
def rabat_5_produktow(cena):
    print("(ilość produktów w koszyku wynosi 5 lub więcej.\nNaliczono 5% rabatu)")
    return round(cena*95/100, 2)

#R3 rabat kwota > 500 15%
def rabat_500(cena):
    print("(kwota zakupów jest równa lub przekroczyła 500 PLN. Naliczono 15 % rabatu)")
    return round(cena*85/100, 2)


def suma_koszyka(kosz):
    sum = 0
    il_wszyst_prod = 0
    nabial = 0
    for poz in kosz:
        c = poz['cena']
        il = poz['ilosc']
        if poz['nazwa'] == "mleko" or "ser":
            nabial += il
        poz_cena = c * il
        il_wszyst_prod += il
    sum = sum + poz_cena
    print("Cena bez rabatu :\n",sum)
    print("Cena z naliczonym rabatem :")

    if nabial >=3:
        return rabat_nabial(sum)
    elif il_wszyst_prod>=5:
        return rabat_5_produktow(sum)
    elif sum>=500:
        return rabat_500(sum)
    else:
        print("brak rabatów")
        return sum




# python koszyk1.py
if __name__ == "__main__":
    koszyk = [
        {'nazwa' : 'banany', 'ilosc': 1, 'cena' : 2.50},
        {'nazwa' : 'ser','ilosc': 1, 'cena' : 3.20},
        {'nazwa' : 'sok','ilosc': 3, 'cena' : 5.00},
        {'nazwa' : 'szynka', 'ilosc': 1,'cena' : 4.50},
        {'nazwa' : 'czekolada','ilosc': 5, 'cena' : 4.20}
    ]

    sum = suma_koszyka(koszyk)
    print(sum)
