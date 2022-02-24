import os
import matplotlib.pyplot as plt
import statistics as stats
import numpy as np
import sys


video=sys.argv[1]
piso=sys.argv[2]
rate=sys.argv[3]
gop=sys.argv[4]
fps=sys.argv[5]
flag=sys.argv[6]



#video="news_cif"
codec= ['h264', 'h265', 'VP8', 'VP9']
#piso="7"

if flag=='0':
    direc = "csv_through"
else:
    direc = "csv_through_ffmpeg"
    
os.chdir(direc)


media =[]
liminf=[]
limsup=[]

sim=['1','2','3','4','5']
eje_x = ['H264', 'H265', 'VP8', 'VP9']

for i in codec:
    promc=[]
    for jj in sim:   
        arch = 'through_'+video+"_"+i+'_'+rate+'_'+fps+'_'+gop+'_piso'+piso+"_sim"+jj+".csv"
        file= open(arch)
        datos = file.readlines()
        thr=[]
        
        for ii in datos:
            pal = ii.find("bps=")
            through = ii[pal+4:len(ii)]
            through = float(through)
            through = round(through/1000,2)
            thr.append(through)
            
        prom = stats.mean(thr)
        prom=round(prom,2)
        promc.append(prom)
    
    prom1=round(stats.mean(promc),2)
    media.append(prom1)
    desviacion = np.std(promc, 0)
    liminfv = round(prom1 - 1.96*(desviacion/np.sqrt(len(promc))),2)
    liminf.append(liminfv)
    limsupv = round(prom1 + 1.96*(desviacion/np.sqrt(len(promc))),2)
    limsup.append(limsupv)
    
        

plt.bar(eje_x,media,color = ["#f44265","#33B2FF","#aaaaff","#9fff7c"])
for i in range(len(media)):
    plt.annotate(str(media[i]), xy=(eje_x[i],media[i]), ha='left', va='bottom')
    
e=list(np.array(limsup) - np.array(media))
plt.errorbar(eje_x, media, yerr=e, fmt='_', ecolor="k",capsize=3)

## Legenda en el eje y
plt.ylabel('Throughput [Kbps]', fontsize=14)
 
## Legenda en el eje x
plt.xlabel('Códecs', fontsize=14)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
#plt.show()
## Mostramos Gráfica
direc = "figuras" #cambiar
os.chdir(direc)
plt.savefig('throu_'+str(video)+"_piso"+piso+'_PROM'+".svg",format="svg")