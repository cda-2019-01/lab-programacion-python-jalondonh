##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
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
col5listsub = [x.split(':') for x in col5list]
col5dict = dict()
for x in col5listsub:
    if x[0] in col5dict:
        col5dict[x[0]].append(int(x[1]))
    else:
        col5dict[x[0]] = [int(x[1])]

for key,value in sorted(col5dict.items()):
    print(key,min(col5dict[key]),max(col5dict[key]),sep=',')

