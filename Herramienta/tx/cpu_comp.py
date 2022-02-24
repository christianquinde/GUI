import matplotlib.pyplot as plt
import numpy as np
import sys, math, os
import statistics as stats

video = sys.argv[1]
#video ='foreman_cif'
codec=['h264','h265','VP8','VP9']
#piso='3'
piso = sys.argv[2]
flag = sys.argv[3]
sim = sys.argv[4]

eje_x = ['H264', 'H265', 'VP8', 'VP9']
media =[]

if flag=='0':
    for j in codec:
        arch="CPU/cpu_usage_"+str(video)+"_"+j+"_piso"+piso+"_sim"+str(sim)+".txt"
        
        file= open(arch)
        datos = file.readlines()
        
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
    for j in codec:
        arch="CPU_ffmpeg/cpu_usage_"+str(video)+"_"+j+"_piso"+piso+"_sim"+str(sim)+".txt"
        
        file= open(arch)
        datos = file.readlines()
        
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

plt.bar(eje_x, media,color = ["indianred","limegreen","lightseagreen","skyblue"])
for i in range(len(media)):
    plt.annotate(str(media[i]), xy=(eje_x[i],media[i]), ha='center', va='bottom')

plt.ylabel('Uso de CPU [%]', fontsize=14)
 
## Legenda en el eje x
plt.xlabel('Codec', fontsize=14)
plt.xticks(fontsize = 13)
plt.yticks(fontsize = 13)
#plt.show()
## Mostramos Gráfica
if flag=='0':
    os.chdir("figuras_cpu_comp")
else:
    os.chdir("figuras_cpu_comp_ffmpeg") 

plt.savefig('cpu_'+str(video)+"_piso"+piso+"_sim"+str(sim)+".png")
    #plt.show()

#print(str(round(prom,4)))