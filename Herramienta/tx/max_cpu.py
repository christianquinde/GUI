import os,sys, math

video = sys.argv[1]
codec = sys.argv[2]
piso = sys.argv[3]
flag = sys.argv[4]
sim = sys.argv[5]


if flag=='0':
    arch="CPU/cpu_usage_"+str(video)+"_"+codec+"_piso"+piso+"_sim"+str(sim)+".txt"

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

    print(str(maxv))
else:
    arch="CPU_ffmpeg/cpu_usage_"+str(video)+"_"+codec+"_piso"+piso+"_sim"+str(sim)+".txt" 

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

    print(str(maxv))

