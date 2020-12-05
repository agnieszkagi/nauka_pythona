#! /usr/bin/python3

produkty = ['mleko', 'chleb', 'sok', 'duza czekolada']
ceny = [3.15, 2, 3.5, 6]
do_zaplaty =+ sum(ceny)
print("Cena bez rabatu : ", do_zaplaty)
print("==============================")
if sum(ceny)>=500:
    print("Naliczono rabat 10%. \nDo zaplaty : ", do_zaplaty*90/100)
if len(produkty)>3:
    print("Naliczono rabat 5%. \nDo zaplaty : ", do_zaplaty*95/100)
