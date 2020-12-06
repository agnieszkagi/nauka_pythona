#!/bin/python3

produkty = [{'nazwa' : 'mleko', 'wartosc' : 2.50},
        {'nazwa' : 'ser', 'wartosc' : 3.20},
        {'nazwa' : 'sok', 'wartosc' : 5},
        {'nazwa' : 'szynka', 'wartosc' : 4.50},
        {'nazwa' : 'czekolada', 'wartosc' : 4.20}
            ]
suma = []
nazwy =[]

for produkt in produkty:
    suma.append(produkt['wartosc'])
    nazwy.append(produkt['nazwa'])
#R1 Rabat 10% na nabial
if 'ser' in nazwy and 'mleko' in nazwy:
    print("Naliczono rabat na nabial 10%. \nDo zaplaty: ", sum(suma)*9/10)
#R2 Rabat 15% - kwota zakupow > 500 PLN
elif sum(suma)>=500:
    print("Naliczono rabat 20%. \nDo zaplaty: ", sum(suma)*85/100)
#R3 Wiecej niz 10 produktow w koszyku rabat 10%
elif len(nazwy)>=10:
    print("Naliczono rabat 20% (wiecej niz 10 produktow). \nDo zaplaty: ", sum(suma)*9/100)
else:
    print("Do zapłaty : ", sum(suma))
