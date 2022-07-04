# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 12:05:34 2022

@author: Lud
"""

import os
os.system('cls||clear')

with open('datasets.txt') as f:
    lines = f.readlines()

lines = lines[1:]
nsets = 0
nset = 0
posi = []
param = []
for j, i in enumerate(lines):
    if i == "\n":
        nset = nset + 1
        posi.append(j)
        param.append(i)
    else:
        lst_aux = i.split("=")
        for i in range(len(lst_aux)):
            lst_aux[i] = lst_aux[i].strip()
            
        param.append(lst_aux)

nparam = posi[1] - posi[0] - 1
## READ INFO
fnames = []
names = []
objects = []
info = []
for i in range(len(posi) - 1):
    indx_beg = posi[i]
    fnames.append(param[indx_beg + 1][1])
    names.append(param[indx_beg + 2][1])
    objects.append(param[indx_beg + 3][1])
    info.append(param[indx_beg + 4][1])
    
## SHOW INFO
for j,i in enumerate(names):
    print(j+1, i)
what_show = int(input("Escoje el set que deseas más info>> "))
u = what_show-1
os.system('cls||clear')
print("NOMBRE: ", names[u])
print("OBJETOS: ", objects[u])
print("INFORMACIÓN: \n", info[u])
print("NOMBRE ARCHIVO: ", fnames[u])
ii = input("Deseas algo mas?")
