import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import statistics as stats

video = sys.argv[1]
#video ='foreman_cif'
codec=['h264','h265','VP8','VP9']
#piso='3'
#flag='0'
piso = sys.argv[2]
flag = sys.argv[3]
sim=['1','2','3','4','5']
eje_x = ['H264', 'H265', 'VP8', 'VP9']


liminf=[]
limsup=[]
promc=[]
for j in codec:
    media=[]
    for jj in sim:
        
        if flag=='0':
            arch = "CPU/cpu_usage_"+str(video)+"_"+j+"_piso"+piso+"_sim"+jj+".txt"
            f=open(arch)
            datos = f.readlines()
        
            cpu_valor=[]
            
            for i in datos:
                buscar=i.find('gst')
                if buscar>0:
                    pos1=i.find("S")
                    if pos1>0:
                        pos2=i.find(" ",pos1+4)
                        valor=i[pos1+1:pos2]
                        valor=valor.replace(',','.')
                        valorf=float(valor)
                        cpu_valor.append(valorf)
                
            maxv=max(cpu_valor)
            media.append(maxv)
        else:
            arch = "CPU_ffmpeg/cpu_usage_"+str(video)+"_"+j+"_piso"+piso+"_sim"+jj+".txt"
            
            f=open(arch)
            datos = f.readlines()
        
            cpu_valor=[]
            
            for i in datos:
                buscar=i.find('ffmpeg')
                if buscar>0:
                    pos1=i.find("S")
                    if pos1>0:
                        pos2=i.find(" ",pos1+4)
                        valor=i[pos1+1:pos2]
                        valor=valor.replace(',','.')
                        valorf=float(valor)
                        cpu_valor.append(valorf)
                
            maxv=max(cpu_valor)
            media.append(maxv)
        
        
    prom = stats.mean(media)
    prom=round(prom,2)
    promc.append(prom)
    

    desviacion = np.std(media, 0)
    liminfv = round(prom - 1.96*(desviacion/np.sqrt(len(media))),2)
    liminf.append(liminfv)
    limsupv = round(prom + 1.96*(desviacion/np.sqrt(len(media))),2)
    limsup.append(limsupv)

plt.bar(eje_x,promc,color = ["#f44265","#33B2FF","#aaaaff","#9fff7c"])
for i in range(len(promc)):
    plt.annotate(str(promc[i]), xy=(eje_x[i],promc[i]), ha='left', va='bottom')
    
e=list(np.array(limsup) - np.array(promc))
plt.errorbar(eje_x, promc, yerr=e, fmt='_', ecolor="k",capsize=3)

plt.ylabel('Uso de CPU [%]', fontsize=14)
plt.xlabel('Tiempo [seg]', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
if flag=='0':
    os.chdir("figuras_cpu_comp")
else:
    os.chdir("figuras_cpu_comp_ffmpeg")

plt.savefig('cpu_'+str(video)+"_piso"+piso+'_PROM'+".svg",format="svg")