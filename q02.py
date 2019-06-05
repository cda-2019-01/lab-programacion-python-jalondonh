##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
import csv
import collections
x = open('data.csv','r').readlines()
y=[z[0] for z in sorted(x[0:])]
frecuencia = collections.Counter(y)
for key,value in frecuencia.items():
     print (key,value,sep=",")




