#!/bin/python3


produkty = [{'nazwa' : 'mleko', 'wartosc' : 2.50},
        {'nazwa' : 'ser', 'wartosc' : 3.20},
        {'nazwa' : 'sok', 'wartosc' : 4}]
suma = []
nazwy =[]

for produkt in produkty:
    suma.append(produkt['wartosc'])
    nazwy.append(produkt['nazwa'])

if 'ser' and 'mleko' in nazwy: 
    print("Naliczono rabat 10%. \nDo zaplaty: ", sum(suma)*9/10)
else:
    print("Do zapłaty : ", sum(suma))
