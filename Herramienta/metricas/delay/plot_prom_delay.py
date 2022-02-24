# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 15:25:21 2021

@author: Christian Quinde
"""
import matplotlib.pyplot as plt
import sys, os
import statistics as stats
import numpy as np
#video='foreman_cif'
#codec='h264'
video = sys.argv[1]
codec=['h264','h265','VP8','VP9']
piso = sys.argv[2]
flag = sys.argv[3]
sim=['1', '2', '3', '4' , '5']
        
array=[]
limsup=[]
liminf=[]
data1=[]
for i in codec:
    for j in sim:
        if flag=='0':
            arch = str(video)+"_"+i+"_piso"+piso+"_sim"+j+".csv"
        else:
            os.chdir("../delay_ffmpeg")
            arch = str(video)+"_"+i+"_piso"+piso+"_sim"+j+".csv"

        with open(arch) as f:
            datos = f.read().splitlines()    
        data = [float(i) for i in datos]
        data1.append(data[0])
    
    prom = stats.mean(data1)
    prom = round(prom,2)
    array.append(prom)
    
    desviacion = np.std(data1, 0)
    liminfv = round(prom - 1.96*(desviacion/np.sqrt(len(data1))),2)
    liminf.append(liminfv)
    limsupv = round(prom + 1.96*(desviacion/np.sqrt(len(data1))),2)
    limsup.append(limsupv)

plt.bar(codec,array,color = ["#f44265","#33B2FF","#aaaaff","#9fff7c"])

# calling the function to add value labels
#addlabels(codec, array)

for i in range(len(array)):
        plt.annotate(str(array[i]), xy=(codec[i],array[i]), ha='left', va='bottom')
e=list(np.array(limsup) - np.array(array))
plt.errorbar(codec, array, yerr=e, fmt='_', ecolor="k",capsize=3)
# giving title to the plot
#plt.title("Comparativa Delay Promedio - "+str(video))
# giving X and Y labels
plt.xlabel("Códecs", fontsize=14)
plt.ylabel("Delay [ms]", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig('delay_'+str(video)+"_piso"+piso+"_PROM.svg",format="svg")
#plt.show()