# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 18:41:04 2022

@author: HP
"""

from astropy.time import Time
from config import *
import numpy as np


def reconst(a):
    aux = a[0] + (a[1]/60) + (a[2]/3600)
    return aux


#reconstruct  night_start and night_ends
night_start_dec = reconst(night_start)
night_ends_dec = reconst(night_ends)

# CALCULATE TIME OF DARKNESS (in decimal hours)
# from start to 24
dark_time = 24 - night_start_dec + night_ends_dec


### CALCULATE TIME DELTA FOR LINSPACE
# in minutes to hours
dtime = dtime/60


if_day = input("¿Quieres observar esta noche?(Y/N) :  ")

if if_day == "Y":

    # in the case we want the same day
    nt = Time.now()
    y, m, d = nt.ymdhms[0], nt.ymdhms[1], nt.ymdhms[2]
    
elif if_day == "N":
    # if we put an input

    a = input("Ingrese la fecha: AÑO, MES, DIA >>  ")
    a = a.split(",")
    a = [int(i) for i in a]
    y, m, d = a[0], a[1], a[2]

h, mi, s = night_start[0], night_start[1], night_start[2]
tim = {'year': y, 'month': m, 'day': d, 'hour' : h, 'minute' : mi, 'second' : s}
tim_ob = Time(tim, format = "ymdhms")

### ---------------------------------
### CREATION OF THE LINSPACE

## for sidereal time
long = str(long) + "d"
sid_beg = tim_ob.sidereal_time("apparent", longitude = long)
sid_beg = sid_beg.hour
sid_end = sid_beg + dark_time
"""
if sid_end > 24:
    sid_end = sid_end - 24
"""
beg = float(sid_beg); fin = float(sid_end)
sid_space = np.arange(beg, fin, dtime)


# for civil hour
civil_space = np.arange(night_start_dec, night_start_dec + dark_time, dtime)


## checking that we aren't ahead of 24h
for j,i in enumerate(civil_space):
    if i>24:
        civil_space[j] = i - 24
    if sid_space[j]>24:
        sid_space[j] = sid_space[j] - 24
    


