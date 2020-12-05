#!/bin/python3


warzywa = ['ogorek', 'baklazan', 'pomidor', 'cebula']
ilosc = [3, 5, 1, 0]

for s in warzywa:
  print(s)
for idx in range( len(warzywa) ) :
  print("idx: " + str(idx) + " : " + warzywa[idx])

for idx in range( len(warzywa) ) :
  print("idx: {0} {1}".format(idx, warzywa[idx]))
  print("nazwa warzywa : " + warzywa[idx] + "\n ilosc : " + str(ilosc[idx]))
