#! /usr/bin/python3

pobrane_haslo = input("Wpisz haslo : ")


if pobrane_haslo == '':
    print("Nie wpisano hasla")
elif len(pobrane_haslo)<=3:
    print("Haslo jest za krotkie")
else:
    print(pobrane_haslo[0]+'*'*(len(pobrane_haslo)-2)+pobrane_haslo[-1])
