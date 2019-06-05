##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
import csv
import collections
import re
from itertools import repeat
data = open('data.csv','r').readlines()
data = [row[0:-1] for row in data]
patron = re.compile('\t|\s+')
datasub = [re.sub(patron,'~',x) for x in data]
datasplit = [re.split('~',x) for x in datasub]
datacol0y4 = [[x[0],x[4]] for x in datasplit]
patron1 = re.compile('[a-z]{3}:')
datasub1 = [[x[0],re.sub(patron1,'',x[1])] for x in datacol0y4]
datasplit = [[x[0],re.split(',',x[1])] for x in datasub1]
datasuma0y4int = [[x[0], sum(list(map(int,x[1])))] for x in datasplit]

for x in datasuma0y4int:
    print(x[0],x[1],sep=',')