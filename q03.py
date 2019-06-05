##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
import csv
import collections
dato = open('data.csv','r').readlines()
k=[z[0] for z in (dato[0:])]
v=[int(z[2]) for z in (dato[0:])]
lista=[]
for i in range(len(k)):
    lista.append([k[i],v[i]])

listadict= dict()

for i in lista:
    if i[0] in listadict:
        listadict[i[0]]+=i[1]
    else:
        listadict[i[0]]=i[1]

listadictorder= sorted(list(listadict))

for key in listadictorder:
    print(key,listadict[key],sep=',')
