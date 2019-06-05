##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
import csv
import collections
import re
data = open('data.csv','r').readlines()
data = [row[0:-1] for row in data]
patron = re.compile('\t|\s+')
datasub = [re.sub(patron,'~',x) for x in data]
datasplit = [re.split('~',x) for x in datasub]
datacol1y2 =[[x[0],x[1]]for x in datasplit]
listadict= dict()
for i in datacol1y2:
    if i[0] in listadict:
        listadict[i[0]].append(int(i[1]))
    else:
        listadict[i[0]] = [int(i[1])]

for key,value in sorted(listadict.items()):
    print(key,max(listadict[key]),min(listadict[key]),sep=',')

