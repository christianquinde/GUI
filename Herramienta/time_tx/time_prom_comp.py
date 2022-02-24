import os
import sys
import matplotlib.pyplot as plt
import statistics as stats
import numpy as np

video=sys.argv[1]
piso=sys.argv[2]
flag=sys.argv[3]



#video="news_cif"
codec= ['h264', 'h265', 'VP8', 'VP9']
#piso="7"

#direc = "time" #cambiar
#os.chdir(direc)


sim=['1','2','3','4','5']
eje_x = ['H264', 'H265', 'VP8', 'VP9']


media =[]
liminf=[]
limsup=[]
cont=1
for i in codec:
    promc=[]
    tx_time =[]
    for jj in sim:  
        if flag=='0':
            arch = video+"_"+i+'_piso'+piso+"_sim"+jj+".txt"
            file= open(arch)
            datos = file.readlines()
            
            for ii in datos:
                pal = ii.find("Execution ended after")
                if pal>=0:
                    minu = ii[pal+24:pal+26]
                    minu = float(minu)*60
                    time = ii[pal+27:len(ii)]
                    time2 = round(float(time),2)+minu
                    tx_time.append(time2)
        else:
            if i=='h264' and cont==1:
                os.chdir("../time_tx_ffmpeg/time_ffmpeg")
                cont=cont+1
            arch = 'time_'+video+"_"+i+'_piso'+piso+"_sim"+jj+".txt"
            file= open(arch)
            datos = file.read()
            datos = float(datos)
            tx_time.append(datos)
        
        
        prom = stats.mean(tx_time)
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
plt.ylabel('Tiempo de codificación [seg]', fontsize=14)
 
## Legenda en el eje x
plt.xlabel('Códecs', fontsize=14)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
## Mostramos Grรกfica
if flag=='0':
    direc = "figuras_time" #cambiar
else:
    direc = "../figuras_time_ffmpeg" #cambiar
        
os.chdir(direc)
plt.savefig(video+"_"+piso+'_PROM'+".svg",format="svg")