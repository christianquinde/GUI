import os
import sys
import matplotlib.pyplot as plt

video=sys.argv[1]
piso=sys.argv[2]
flag=sys.argv[3]
sim=sys.argv[4]


#video="news_cif"
codec= ['h264', 'h265', 'VP8', 'VP9']
#piso="7"

#direc = "time" #cambiar
#os.chdir(direc)

tx_time =[]
eje_x = ['H264', 'H265', 'VP8', 'VP9']
for i in codec:
    if flag=='0':
        arch = video+"_"+i+'_piso'+piso+"_sim"+str(sim)+".txt"
        file= open(arch)
        datos = file.readlines()
        
        for i in datos:
            pal = i.find("Execution ended after")
            if pal>=0:
                minu = i[pal+24:pal+26]
                minu = float(minu)*60
                time = i[pal+27:len(i)]
                time2 = round(float(time),2)+minu
                tx_time.append(time2)
    else:
        print(os.getcwd())
        if i=='h264':
            os.chdir("../time_tx_ffmpeg/time_ffmpeg")
        print(os.getcwd())
        arch = 'time_'+video+"_"+i+'_piso'+piso+"_sim"+str(sim)+".txt"
        file= open(arch)
        datos = file.read()
        datos = float(datos)
        tx_time.append(datos)

plt.bar(eje_x, tx_time,color = ["indianred","limegreen","lightseagreen","skyblue"])
for i in range(len(tx_time)):
    plt.annotate(str(tx_time[i]), xy=(eje_x[i],tx_time[i]), ha='center', va='bottom')
## Legenda en el eje y
plt.ylabel('Tiempo de codificación [seg]', fontsize=14)
 
## Legenda en el eje x
plt.xlabel('Codec', fontsize=14)
plt.xticks(fontsize = 13)
plt.yticks(fontsize = 13)
## Mostramos Grรกfica
if flag=='0':
    direc = "figuras_time" #cambiar
else:
    direc = "../figuras_time_ffmpeg" #cambiar
        
os.chdir(direc)
plt.savefig(video+"_"+piso+"_sim"+str(sim)+".png")