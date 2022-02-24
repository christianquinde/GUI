# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 17:17:49 2021

@author: Christian Quinde
"""

import sys, math
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout
import subprocess
import os
import time
from segunda2 import Ui_segunda
from tercera import Ui_tercera
import functools
import operator

pwd = os.getcwd()
#print(pwd)

#Creamos una clase para poder Ejecutar nuestra Aplicacion "QMainWindow"
class Gui_Interfaz(QMainWindow):

    #Creamos nuestro constructor
    def __init__(self):
        super().__init__()
        uic.loadUi("herramienta.ui",self)
        self.Btn_cargar.clicked.connect(self.cargar)
        self.Btn_Tx.clicked.connect(self.stream)
        self.Btn_stop.clicked.connect(self.stop)
        self.Btn_Rx.clicked.connect(self.pcaps)
        self.Btn_metrics.clicked.connect(self.metrics)
        self.Btn_plots.clicked.connect(self.plot_comparativa)
        self.Btn_sync.clicked.connect(self.sync)
        self.inputFileButton.clicked.connect(self.onInputFileButtonClicked)
        self.play_video.clicked.connect(self.playvideo)
        self.Btn_plots_tot.clicked.connect(self.plot_tot)
        self.Btn_encode.clicked.connect(self.encode)

        self.photo1 = QtWidgets.QLabel(self.centralwidget)
        self.photo1.setGeometry(QtCore.QRect(170, 270, 321, 271))
        self.photo1.setText("")
        self.photo1.setPixmap(QtGui.QPixmap("cuenca.png"))
        self.photo1.setScaledContents(True)
        self.photo1.setObjectName("photo1")
        
    
    def cargar(self):
        global codec, ip_dst, port, ext, piso, bitrate, gop, fps, sim, flag, ip_src
        os.chdir(pwd)
        codec = self.select_codec.currentItem().text()
        ip_dst = self.ip_dst.text()
        ip_src = self.ip_src.text()
        port = self.port_dst.text()
        piso = self.select_piso.currentItem().text()
        flag = self.select_tool.currentItem().text()
        sim = self.select_sim.currentItem().text()
        if flag=='GStreamer':
            flag=0
        else:
            flag=1

        conf_file = "tesis.conf"
        file = open(conf_file)
        config = file.readlines()
        bitrate = config[0]
        bitrate = bitrate[8:len(bitrate)-1]
        gop = config[1]
        gop = gop[4:len(gop)-1]
        fps = config[2]
        fps = fps[4:len(fps)-1]

        if str(codec) == 'h264' or str(codec) == 'h265':
            ext='mp4'
        else:
            ext='webm'
        os.chdir(str(pwd)+'/Herramienta/tx')
        self.tx_label.setText('Enviando Video: '+str(video)+"_"+str(codec)+"."+ext+"  "+"Exp:"+str(sim))
        
    
    def stream(self):
        os.chdir(str(pwd)+'/Herramienta/tx')
        subprocess.run(['./transmitir_videos.sh',str(video),str(codec),str(ip_dst),str(port),ext,str(piso), str(path), str(bitrate), str(gop), str(fps), str(flag), str(sim), str(ip_src)])
        
    
    def stop(self):
        os.chdir(str(pwd)+'/Herramienta/tx')
        subprocess.run(['./kill.sh',str(video),str(codec),str(piso), str(bitrate), str(gop), str(fps), str(flag), str(sim)])
        #os.chdir('../..')

    def pcaps(self):
        os.chdir(str(pwd))
        subprocess.run(['./receive_pcaps.sh',str(video),str(codec),str(piso), str(bitrate), str(gop), str(fps), str(flag), str(sim)])


    def metrics(self):
        os.chdir(str(pwd)+'/Herramienta/tx')
        cpu=subprocess.run(['python3','max_cpu.py',str(video),str(codec),str(piso),str(flag), str(sim)],capture_output=True) #   'python', 'somescript.py', somescript_arg1, somescript_val1,...]
        os.chdir(str(pwd)+'/Herramienta')
        delay=subprocess.run(['python3','delayypl.py',str(video),str(codec),str(piso), str(bitrate), str(gop), str(fps), str(flag), str(sim)],capture_output=True) #   'python', 'somescript.py', somescript_arg1, somescript_val1,...]
        throu=subprocess.run(['python3','throughput.py',str(video),str(codec),str(piso), str(bitrate), str(gop), str(fps), str(flag), str(sim)],capture_output=True)
        time_tx=subprocess.run(['python3','timetx.py',str(video),str(piso),str(codec),str(flag), str(sim)],capture_output=True)
        os.chdir('..')
        print('throu='+str(throu))
        print('delay='+str(delay))
        print('cpu='+str(cpu))
        print('time_tx='+str(time_tx))
        aaa=delay.stdout.decode().split()
        bbb=throu.stdout.decode()
        ccc=time_tx.stdout.decode()
        ddd=cpu.stdout.decode()
        
        if flag==0:
            self.photo1.setPixmap(QtGui.QPixmap(str(pwd)+"/Herramienta/figuras_throu/"+str(piso)+"_"+str(video)+"_"+str(codec)+"_sim"+str(sim)+".png"))
        else:
            self.photo1.setPixmap(QtGui.QPixmap(str(pwd)+"/Herramienta/figuras_throu_ffmpeg/"+str(piso)+"_"+str(video)+"_"+str(codec)+"_sim"+str(sim)+".png"))
        
        self.delay_label.setText(aaa[0])
        self.pl_label.setText(aaa[1])
        self.thr_label.setText(bbb)
        self.time_label.setText(ccc)
        self.cpu_label.setText(ddd)
        subprocess.run(['./print_delay.sh',str(video),aaa[0],aaa[1],str(codec),str(piso),str(flag), str(sim)])

    def plot_comparativa(self):
        os.chdir(str(pwd))
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_segunda()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def plot_tot(self):
        os.chdir(str(pwd))
        self.ventana2=QtWidgets.QMainWindow()
        self.ui=Ui_tercera()
        self.ui.setupUi(self.ventana2)
        self.ventana2.show()

    def sync(self):
        os.chdir(str(pwd)+'/Herramienta')
        subprocess.run(['./sync.sh',str(ip_dst)])
    
    def onInputFileButtonClicked(self):
        global video, path
        os.chdir(pwd)
        file_filter = '*.yuv'
        filename = QFileDialog.getOpenFileNames(
            parent=self,
            caption='Select a video file',
            directory=os.chdir('..'),
            filter=file_filter
        )
        if filename:
            video_arch = [tup[0] for tup in filename]
            video_arch1 = video_arch[0]
            self.inputFileLineEdit.setText(video_arch1) 
            rep = video_arch1.count('/')
            pos1=0
            for x in range(0,rep):
                pos = video_arch1.find('/',pos1)
                pos1 = pos+1
            video = video_arch1[pos+1:len(video_arch1)-4]
            path = video_arch1[0:pos+1]

    def playvideo(self):
        if flag==0:
            os.chdir(str(pwd)+'/Herramienta/PSNR/video')
            subprocess.run(['./playvid.sh',str(video),str(codec), str(bitrate), str(gop), str(fps), str(flag)])
        else:
            os.chdir(str(pwd)+'/Herramienta/PSNR/video_ffmpeg')
            subprocess.run(['./playvid.sh',str(video),str(codec), str(bitrate), str(gop), str(fps), str(flag)])

    def encode(self):
        os.chdir(str(pwd)+"/Herramienta/PSNR")
        if flag==0:
            subprocess.run(['./h264_encode_Gst.sh',str(path),str(bitrate),str(gop),str(fps),str(video)])
            subprocess.run(['./h265_encode_Gst.sh',str(path),str(bitrate),str(gop),str(fps),str(video)])
            subprocess.run(['./vp8_encode_Gst.sh',str(path),str(bitrate),str(gop),str(fps),str(video)])
            subprocess.run(['./vp9_encode_Gst.sh',str(path),str(bitrate),str(gop),str(fps),str(video)])        
        else:
            subprocess.run(['./h264_encode_ffmpeg.sh',str(path),str(bitrate),str(gop),str(fps),str(video)])
            subprocess.run(['./h265_encode_ffmpeg.sh',str(path),str(bitrate),str(gop),str(fps),str(video)])
            subprocess.run(['./vp8_encode_ffmpeg.sh',str(path),str(bitrate),str(gop),str(fps),str(video)])
            subprocess.run(['./vp9_encode_ffmpeg.sh',str(path),str(bitrate),str(gop),str(fps),str(video)])        



#Se ejecuta cuando iniciamos el Script
if __name__ == '__main__':
    #Inicia la aplicacion para abrirla y cerrarla
    app = QApplication(sys.argv)
    GUI = Gui_Interfaz()
    #Muestra nuestra aplicacion
    GUI.show()
    #Cierra nuestra aplicacion cuando le damos a cerrar
    sys.exit(app.exec_())