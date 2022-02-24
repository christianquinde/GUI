#import numpy as np
#import pandas as pd
import statistics as stats
import os
#import matplotlib.pyplot as plt
from datetime import datetime
import sys


#video="foreman_cif" #name video
#video="mother-daughter_cif" #name video
#video="news_cif" #name video
video=sys.argv[1]
codec=sys.argv[2]
piso=sys.argv[3]
gop = sys.argv[5] #GoP
fps =sys.argv[6]  #FPS
rate = sys.argv[4] #rate
flag = sys.argv[7]
sim = sys.argv[8]
#video='news_cif'
#codec='h264'
#piso="1"


if flag=='0':
#################################### GStreamer #####################################
    #------- leer tx ---------
    direc = "tx"
    os.chdir(direc)
    direcint = "csv"
    os.chdir(direcint)


    arch = video+"_"+codec+"_"+str(rate)+"_"+str(fps)+"_"+str(gop)+"_piso"+piso+"_sim"+str(sim)+".csv"
    file= open(arch,"r")
    datos = file.readlines()

    rtcpnum = len(datos)

    arrayfechatx = []

    for i in range(0,rtcpnum):
        leer = datos[i] 
        pos1 = leer.find("2022")
        pos1 = pos1+5
        pos2 = leer.find("-")
        pos2 = pos2-4
        fecha = leer[pos1:pos2]
        remp = fecha.replace(".",":")
        arrayfechatx.append(remp)
         

    #------- leer rx ---------
    os.chdir("..")
    os.chdir("..")
    direc2 = "rx"
    os.chdir(direc2)
    direcint2 = "csv"
    os.chdir(direcint2)



    file= open(arch,"r")
    datos = file.readlines()

    rtcpnum = len(datos)

    arrayfecharx = []

    for i in range(0,rtcpnum):
        leer = datos[i] 
        pos1 = leer.find("2022")
        pos1 = pos1+5
        pos2 = leer.find("-")
        pos2 = pos2-4
        fecha = leer[pos1:pos2]
        remp = fecha.replace(".",":")
        arrayfecharx.append(remp)

    #------ delay ----------
    delay = []
    value = 100000
    for gg in range(0,len(arrayfecharx)):
        format = '%H:%M:%S:%f'
        resta = datetime.strptime(arrayfechatx[len(arrayfechatx)-1], format)-datetime.strptime(arrayfecharx[gg], format)
        del1 = str(resta)
        enc = del1.find("y")
        if enc < 1:
            min=del1 [2:4]
            min=float(min)*60
            del2 = del1 [5:len(del1)] 
            dels = (float(del2)+min) *1000
            if dels >0:
                if dels < value:
                    value = dels
                    position=gg
                
            
            
    arrayfecharx = arrayfecharx[position+1-len(arrayfechatx):position+1]

    for i in range(0,len(arrayfechatx)):
        format = '%H:%M:%S:%f'
        delaynum = datetime.strptime(arrayfechatx[i], format)-datetime.strptime(arrayfecharx[i], format)
        delays1 = str(delaynum)
        encontrar = delays1.find('y')
        if encontrar<0:
            delays2 = delays1 [5:len(delays1)] 
            delays = float(delays2) *1000 #milisegundos
            delays = round(delays,2)
            delay.append(delays)

    mediavv = stats.mean(delay)
    #desviacion = np.std(delay, 0)
    #liminfv = mediavv - 1.96*(desviacion/np.sqrt(len(delay)))
    #limsupv = mediavv + 1.96*(desviacion/np.sqrt(len(delay)))

    # --------------------------- PL ------------

    os.chdir("..")
    os.chdir("..")
    direc2 = "tx"
    os.chdir(direc2)
    direcint2 = "csv_total"
    os.chdir(direcint2)

    arch = "total_"+video+"_"+codec+"_"+str(rate)+"_"+str(fps)+"_"+str(gop)+"_piso"+piso+"_sim"+str(sim)+".csv"
    file= open(arch,"r")
    datos = file.readlines()

    txpl = len(datos)


    os.chdir("..")
    os.chdir("..")
    direc2 = "rx"
    os.chdir(direc2)
    direcint2 = "csv_total"
    os.chdir(direcint2)

    file= open(arch,"r")
    datos = file.readlines()

    rxpl = len(datos)

    pl = txpl-rxpl # paquetes perdidos 

    plpor = (pl*100)/txpl  # pl en porcentaje

    print(str(round(mediavv,4)))
    print(str(round(plpor,4)))    



#################################### FFMPEG #####################################
else:
    #------- leer tx ---------
    direc = "tx"
    os.chdir(direc)
    direcint = "csv_ffmpeg"
    os.chdir(direcint)


    arch = video+"_"+codec+"_"+str(rate)+"_"+str(fps)+"_"+str(gop)+"_piso"+piso+"_sim"+str(sim)+".csv"
    file= open(arch,"r")
    datos = file.readlines()

    rtcpnum = len(datos)

    arrayfechatx = []

    for i in range(0,rtcpnum):
        leer = datos[i] 
        pos1 = leer.find("2022")
        pos1 = pos1+5
        pos2 = leer.find("-")
        pos2 = pos2-4
        fecha = leer[pos1:pos2]
        remp = fecha.replace(".",":")
        arrayfechatx.append(remp)
         

    #------- leer rx ---------
    os.chdir("..")
    os.chdir("..")
    direc2 = "rx"
    os.chdir(direc2)
    direcint2 = "csv_ffmpeg"
    os.chdir(direcint2)



    file= open(arch,"r")
    datos = file.readlines()

    rtcpnum = len(datos)

    arrayfecharx = []

    for i in range(0,rtcpnum):
        leer = datos[i] 
        pos1 = leer.find("2022")
        pos1 = pos1+5
        pos2 = leer.find("-")
        pos2 = pos2-4
        fecha = leer[pos1:pos2]
        remp = fecha.replace(".",":")
        arrayfecharx.append(remp)

    #------ delay ----------
    delay = []
    value = 100000
    for gg in range(0,len(arrayfecharx)):
        format = '%H:%M:%S:%f'
        resta = datetime.strptime(arrayfechatx[len(arrayfechatx)-1], format)-datetime.strptime(arrayfecharx[gg], format)
        del1 = str(resta)
        enc = del1.find("y")
        if enc < 1:
            del2 = del1 [5:len(del1)] 
            dels = float(del2) *1000
            if dels >0:
                if dels < value:
                    value = dels
                    position=gg
                
            
            
    arrayfecharx = arrayfecharx[position+1-len(arrayfechatx):position+1]

    for i in range(0,len(arrayfechatx)):
        format = '%H:%M:%S:%f'
        delaynum = datetime.strptime(arrayfechatx[i], format)-datetime.strptime(arrayfecharx[i], format)
        delays1 = str(delaynum)
        encontrar = delays1.find('y')
        if encontrar<0:
            delays2 = delays1 [5:len(delays1)] 
            delays = float(delays2) *1000 #milisegundos
            delays = round(delays,2)
            delay.append(delays)

    mediavv = stats.mean(delay)
    #desviacion = np.std(delay, 0)
    #liminfv = mediavv - 1.96*(desviacion/np.sqrt(len(delay)))
    #limsupv = mediavv + 1.96*(desviacion/np.sqrt(len(delay)))

    # --------------------------- PL ------------

    os.chdir("..")
    os.chdir("..")
    direc2 = "tx"
    os.chdir(direc2)
    direcint2 = "csv_total_ffmpeg"
    os.chdir(direcint2)

    arch = "total_"+video+"_"+codec+"_"+str(rate)+"_"+str(fps)+"_"+str(gop)+"_piso"+piso+"_sim"+str(sim)+".csv"
    file= open(arch,"r")
    datos = file.readlines()

    txpl = len(datos)


    os.chdir("..")
    os.chdir("..")
    direc2 = "rx"
    os.chdir(direc2)
    direcint2 = "csv_total_ffmpeg"
    os.chdir(direcint2)

    file= open(arch,"r")
    datos = file.readlines()

    rxpl = len(datos)

    pl = txpl-rxpl # paquetes perdidos 

    plpor = (pl*100)/txpl  # pl en porcentaje

    print(str(round(mediavv,4)))
    print(str(round(plpor,4)))  

