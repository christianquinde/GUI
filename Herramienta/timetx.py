# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 16:53:54 2021

@author: Paul Astudillo
"""

import os
import sys



video=sys.argv[1]
piso=sys.argv[2]
codec=sys.argv[3]
flag=sys.argv[4]
sim=sys.argv[5]

if flag=='0':
    direc = "time_tx"
    os.chdir(direc)

    arch = video+"_"+codec+"_"+"piso"+piso+"_sim"+str(sim)+".txt"
    file= open(arch)
    datos = file.readlines()

    for i in datos:
        pal = i.find("Execution ended after")
        if pal>=0:
            time = i[pal+25:len(i)]

    file = open("time/time_"+video+"_"+codec+"_piso"+piso+"_sim"+str(sim)+".txt", "w")
    file.write(time)
    file.close()
    print(str(time))


else:
    direc = "time_tx_ffmpeg"
    os.chdir(direc)

    arch = video+"_"+codec+"_"+"piso"+piso+"_sim"+str(sim)+".txt"
    file= open(arch)
    datos = file.readlines()
    contar=0    
    contar2 = 0
    for j in datos:
        contar3 = j.find('time=')
        if contar3>0:
            contar=contar+1
        
    
    for i in datos:
        busqueda=i.find('time=')
        if busqueda>0:
            contar2=contar2+1
        
        if contar2==contar:
            pal = i.find("time=")
            if pal>=0:
                time = i[pal+11:pal+16]

    file = open("time_ffmpeg/time_"+video+"_"+codec+"_piso"+piso+"_sim"+str(sim)+".txt", "w")
    file.write(str(time))
    file.close()
    print(str(time))
