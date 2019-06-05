##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
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
datacol3y1 = [[x[3],int(x[1])] for x in datasplit]
repeated = [x for item in datacol3y1 for x in repeat(item[0], item[1])]
repeatedsplit = [re.split(',',x) for x in repeated]
repeatedsplit_flatten = [y for x in repeatedsplit for y in x]
sortedlist = sorted(repeatedsplit_flatten)
countsortedlist=[[x,sortedlist.count(x)] for x in set(sortedlist)]
for x in sorted(countsortedlist):
    print(x[0],x[1],sep=',')
