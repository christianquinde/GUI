# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:30:06 2021

@author: Christian Quinde
"""
import numpy as np
#import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt
import os
import sys
 
n_frames = 300 # numero de frames
#video = "news_cif"
#piso = "7"
video = sys.argv[1]
piso = sys.argv[2]
gop = sys.argv[4] #GoP
fps = sys.argv[5] #FPS
rate = sys.argv[3] #rate
flag = sys.argv[6]
codec = ("h264","h265","VP8","VP9")
 
if flag=='0':
    direc = "logs"
else:
    direc = "logs_ffmpeg"
os.chdir(direc)
video_psnr = []
media = []
liminf = []
limsup = []
for i in codec:
    arch = "psnr_"+video+"_"+str(i)+"_"+str(rate)+"_"+str(fps)+"_"+str(gop)+"_piso"+str(piso)+".log"
    file= open(arch)
    datos = file.read()
    #hallar el valor
    pos1 = 0
    pos2 = 0
    auxi = 0
    nump = 0
    final = 0
    array_psnr = []
     
    for dd in range(0,n_frames):
        pos1 = datos.find("psnr_y:",auxi)
        pos1 = pos1+7
        pos2 = datos.find(" psnr_u:",pos1+1)
        #pos2 = pos2-1
        psnr = datos[pos1:pos2]
        psnr = float(psnr)
        array_psnr.append(psnr)
        auxi = pos1+39
     
    mediav = stats.mean(array_psnr)
    mediav = round(mediav, 2)
    video_psnr.append(mediav)
    
    media.append(mediav)
    desviacion = np.std(array_psnr, 0)
    liminfv = round(mediav - 1.96*(desviacion/np.sqrt(len(array_psnr))),2)
    liminf.append(liminfv)
    limsupv = round(mediav + 1.96*(desviacion/np.sqrt(len(array_psnr))),2)
    limsup.append(limsupv)
    xxx=""

plt.bar(codec,video_psnr,color = ["#f44265","#33B2FF","#aaaaff","#9fff7c"])
for i in range(len(video_psnr)):
    plt.annotate(str(video_psnr[i]), xy=(codec[i],video_psnr[i]), ha='left', va='bottom')
e=list(np.array(limsup) - np.array(video_psnr))
plt.errorbar(codec, video_psnr, yerr=e, fmt='_', ecolor="k",capsize=3)
plt.ylabel('PSNR [dB]', fontsize=14)
plt.xlabel('Códecs', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
if flag=='0':
    os.chdir("../figuras_psnr")
else:
    os.chdir("../figuras_psnr_ffmpeg")
plt.savefig('psnr_'+str(video)+"_piso"+piso+".svg",format="svg")
#plt.show()

# os.chdir("..") 
# resulflow = open("resul_psnr.txt","a") 
# resulflow.write(video+" "+str(video_psnr)+"\n") 
# resulflow.write(video+" "+"[h264, h265, VP8, VP9]")
# resulflow.write("\n") 
# resulflow.write("Límites Inferiores:\n")
# resulflow.write(str(liminf)+"\n") 
# resulflow.write("\n")
# resulflow.write("Límites Superiores:\n")
# resulflow.write(str(limsup)+"\n")  
# resulflow.write("\n") 
# resulflow.close()
