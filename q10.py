##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
import csv
import collections
import re
data = open('data.csv','r').readlines()
data = [row[0:-1] for row in data]
patron = re.compile('\t|\s+')
datasub = [re.sub(patron,'~',x) for x in data]
datasplit = [re.split('~',x) for x in datasub]
datacol5 =[x[4] for x in datasplit]
datacol5split = [re.split(',',x) for x in datacol5]
col5list = [j for i in datacol5split for j in i]
col5listsub = [x.split(':')[0] for x in col5list]
col5listsubsorted = sorted(col5listsub)
frecuencia = collections.Counter(col5listsubsorted)

for key,value in frecuencia.items():
    print(key,value,sep=",")