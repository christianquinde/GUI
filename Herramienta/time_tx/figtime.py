# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 17:19:52 2021

@author: Paul Astudillo
"""

import numpy as np
import pandas as pd
import statistics as stats
import os
import matplotlib.pyplot as plt
import sys

video=sys.argv[1]
piso=sys.argv[2]

direc = "time"
os.chdir(direc)
eje_x = ['H264', 'H265', 'VP8', 'VP9']

file = open("time_"+video+"_"+piso+".txt")
datos = file.readlines()

eje_y=[]
for i in datos:
    min = i[0:2]
    min = min*60
    seg = i[3:10]
    seg =seg+min
    seg = float(seg)
    red = round(seg,3)
    eje_y.append(red)


plt.bar(eje_x, eje_y,color = ["orange","peru","lime","skyblue"])
for i in range(len(eje_y)):
    plt.annotate(str(eje_y[i]), xy=(eje_x[i],eje_y[i]), ha='center', va='bottom')
## Legenda en el eje y
plt.ylabel('Tiempo de Transmisión')
 
## Legenda en el eje x
plt.xlabel('Codec')

## Mostramos Gráfica
plt.show()
plt.savefig(video+"_"+piso+".png")
    
    