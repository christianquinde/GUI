# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:45:01 2021

@author: Paul Astudillo
"""

import statistics as stats
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

video=sys.argv[1]
codec=sys.argv[2]
piso=sys.argv[3]
gop = sys.argv[5] #GoP
fps =sys.argv[6]  #FPS
rate = sys.argv[4] #rate
flag = sys.argv[7]
sim = sys.argv[8]
#video="foreman_cif"
#codec="h264"
#piso="1"

if flag=='0':
#################################### GStreamer #####################################
    direc = "rx/csv_through"
    os.chdir(direc)

    arraygop = []
    ll = []
    arch = "through_"+video+"_"+codec+"_"+str(rate)+"_"+str(fps)+"_"+str(gop)+"_piso"+piso+"_sim"+str(sim)+".csv"
    file= open(arch)
    datos = file.read()
    rep = datos.count("bps=",0,len(datos))
    inic = 0
    p1 = 0
    pf = 2
    while rep!=inic:
        pos1= datos.find("bps=",p1)
        pos1= pos1+4
        final=datos.find("Time:",pf)
        final= final-1
        thr = datos[pos1:final]
        cam = float(thr)
        cam = cam/1000
        arraygop.append(cam)
        p1 = final+5
        pf = final+5
        inic = inic+1

    prom = stats.mean(arraygop)
    vec = np.ones(rep)
    com2 = vec*1600
    vec = vec*prom
    x = np.arange(0,rep/10,0.1)
    dde = round(prom,2)

    plt.plot(x,arraygop,linewidth=0.8,c="#33B2FF")
    plt.plot(x,vec,linewidth=0.8,c="#f44265")     
    plt.ylabel('Throughput [kbps]',fontsize=14)
    plt.xlabel('Tiempo [seg]',fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    wwq="promedio "+codec+"=" +str(dde)
    ll.append(codec)
    ll.append(wwq)

    com = "umbral red Ad-Hoc = 1600"
    ll.append(com)
    #plt.plot(x,com2,linewidth=0.8,linestyle = 'dashed',c="k")
    #plt.legend(ll,loc="upper right")
    os.chdir("..")
    os.chdir("..")
    os.chdir("figuras_throu")
    plt.savefig(piso+"_"+video+"_"+codec+"_sim"+str(sim)+".svg",format="svg")
    #plt.show()
    os.chdir("..")

    prom = stats.mean(arraygop)
    print(str(round(prom,4))) 


else:
#################################### FFMPEG #####################################
    direc = "rx/csv_through_ffmpeg"
    os.chdir(direc)

    arraygop = []
    ll = []
    arch = "through_"+video+"_"+codec+"_"+str(rate)+"_"+str(fps)+"_"+str(gop)+"_piso"+piso+"_sim"+str(sim)+".csv"
    file= open(arch)
    datos = file.read()
    rep = datos.count("bps=",0,len(datos))
    inic = 0
    p1 = 0
    pf = 2
    while rep!=inic:
        pos1= datos.find("bps=",p1)
        pos1= pos1+4
        final=datos.find("Time:",pf)
        final= final-1
        thr = datos[pos1:final]
        cam = float(thr)
        cam = cam/1000
        arraygop.append(cam)
        p1 = final+5
        pf = final+5
        inic = inic+1

    prom = stats.mean(arraygop)
    vec = np.ones(rep)
    com2 = vec*1600
    vec = vec*prom
    x = np.arange(0,rep/10,0.1)
    dde = round(prom,2)

    plt.plot(x,arraygop,linewidth=0.8)
    plt.plot(x,vec,linewidth=0.8)     
    plt.ylabel('Throughput [kbps]')
    wwq="promedio "+codec+"=" +str(dde)
    ll.append(codec)
    ll.append(wwq)

    com = "umbral red Ad-Hoc = 1600"
    ll.append(com)
    plt.plot(x,com2,linewidth=0.8,linestyle = 'dashed')
    plt.legend(ll,loc="upper right")
    os.chdir("..")
    os.chdir("..")
    os.chdir("figuras_throu_ffmpeg")
    plt.savefig(piso+"_"+video+"_"+codec+"_sim"+str(sim)+".png")
    #plt.show()
    os.chdir("..")

    prom = stats.mean(arraygop)
    print(str(round(prom,4))) 


