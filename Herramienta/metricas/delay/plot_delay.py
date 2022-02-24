# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 15:25:21 2021

@author: Christian Quinde
"""
import matplotlib.pyplot as plt
import sys, os

#video='foreman_cif'
#codec='h264'
video = sys.argv[1]
codec=['h264','h265','VP8','VP9']
piso = sys.argv[2]
flag = sys.argv[3]
sim=sys.argv[4]
        
array=[]
for i in codec:
    if flag=='0':
        arch = str(video)+"_"+i+"_piso"+piso+"_sim"+str(sim)+".csv"
    else:
        os.chdir("../delay_ffmpeg")
        arch = str(video)+"_"+i+"_piso"+piso+"_sim"+str(sim)+".csv"

    with open(arch) as f:
        datos = f.read().splitlines()    
    data = [float(i) for i in datos]
    array.append(data[0])
    
plt.bar(codec,array,color = ["indianred","limegreen","lightseagreen","skyblue"])
# calling the function to add value labels
#addlabels(codec, array)
for i in range(len(array)):
        plt.annotate(str(array[i]), xy=(codec[i],array[i]), ha='center', va='bottom')
# giving title to the plot
#plt.title("Comparativa Delay Promedio - "+str(video))
# giving X and Y labels
plt.xlabel("Codecs", fontsize=14)
plt.ylabel("Delay [ms]", fontsize=14)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.savefig('delay_'+str(video)+"_piso"+piso+"_sim"+str(sim)+".png")
#plt.show()