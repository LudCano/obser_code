# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 21:33:06 2022

@author: HP
"""

# IF VISIBLE
import numpy as np
from config import *

def to_rad(a):
    return a*np.pi/180

def if_visible(lat, lst, ar, dec):
    lst = lst[0] + (lst[1]/60) + (lst[2]/3600)
    H = lst-ar
    if H < 0:
        H = H + 24
    H = H*15
    a = np.arcsin(np.sin(to_rad(dec))*np.sin(to_rad(lat)) + np.cos(to_rad(dec))*np.cos(to_rad(lat))*np.cos(to_rad(H)))
    a = a*180/np.pi
    return a #altura en grados

def if_visible_vec(lat, lst, ars, decs):
    aux1 = np.sin(to_rad(lat))
    aux2 = np.cos(to_rad(lat))
    #lst = lst[0] + (lst[1]/60) + (lst[2]/3600) #'cause it's in decimals already
    alturas = []
    indices = []
    for i in range(len(ars)):
        H = lst-ars[i]
        if H < 0:
            H = H + 24
        H = H*15
        a = np.arcsin(np.sin(to_rad(decs[i]))*aux1 + np.cos(to_rad(decs[i]))*aux2*np.cos(to_rad(H)))
        a = a*180/np.pi
        if a >= 0:
            alturas.append(a)
            indices.append(i)
    return alturas, indices #altura en grados


# esto debería venir de otros códigos
sidereal_space = [7.8134, 7.980, 8.1467]
civil_space = [20, 20.16, 20.333]
fnames = ["hip"]


import pandas as pd
df = pd.read_csv(fnames[0])

ars = df["_RAJ2000"]
decs = df["_DEJ2000"]

resultados = []
estrellas = []
for i in sidereal_space:
    aux, aux2 = if_visible_vec(lat, i, ars, decs)
    resultados.append(aux)
    estrellas.append(aux2)








