##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas y sin repetir letra) 
## de la primera  columna que aparecen asociadas a dicho valor de la 
## segunda columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'B', 'D', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
import csv
import collections
import re
import itertools
data = open('data.csv','r').readlines()
data = [row[0:-1] for row in data]
patron = re.compile('\t|\s+')
datasub = [re.sub(patron,'~',x) for x in data]
datasplit = [re.split('~',x) for x in datasub]
datacol2y1 =[[x[1],x[0]]for x in datasplit]
datacol2y1sorted = sorted(datacol2y1)
listadict= dict()
datacol2y1sorted.sort()
datalistunique = list(eval(x) for x in set([str(x) for x in datacol2y1sorted]))

listadict2 = dict()
datalistuniquesorted = sorted(datalistunique)
for i in datalistuniquesorted:
    if i[0] in listadict2:
        listadict2[i[0]].append(i[1])
    else:
        listadict2[i[0]] = [i[1]]

for key,value in sorted(listadict2.items()):
    print((key,value))
