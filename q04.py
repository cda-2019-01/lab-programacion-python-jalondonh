##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
import csv
import collections
import re

data = open('data.csv','r').readlines()
data = [row[0:-1] for row in data]
patron = re.compile('\t|\s+')
datasub = [re.sub(patron,'~',x) for x in data]
datasplit = [re.split('~',x) for x in datasub]
datamonth =[[x[2]][0].split('-')[1] for x in datasplit]
datamonthsorted = sorted(datamonth)
frecuencia = collections.Counter(datamonthsorted)
for key,value in frecuencia.items():
     print (key,value,sep=",")



    