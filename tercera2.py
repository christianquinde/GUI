# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tercera.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout
import os, subprocess, sys


class Ui_tercera(object):
    def setupUi(self, tercera):
        tercera.setObjectName("tercera")
        tercera.resize(1307, 716)
        tercera.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(tercera)
        self.centralwidget.setObjectName("centralwidget")
        self.pl_comp = QtWidgets.QLabel(self.centralwidget)
        self.pl_comp.setGeometry(QtCore.QRect(50, 380, 331, 300))
        self.pl_comp.setText("")
        self.pl_comp.setPixmap(QtGui.QPixmap("cuenca.png"))
        self.pl_comp.setScaledContents(True)
        self.pl_comp.setObjectName("pl_comp")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(170, 350, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(560, 10, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(180, 10, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.thr_comp = QtWidgets.QLabel(self.centralwidget)
        self.thr_comp.setGeometry(QtCore.QRect(50, 40, 331, 300))
        self.thr_comp.setText("")
        self.thr_comp.setPixmap(QtGui.QPixmap("cuenca.png"))
        self.thr_comp.setScaledContents(True)
        self.thr_comp.setObjectName("thr_comp")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(900, 10, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.psnr_comp = QtWidgets.QLabel(self.centralwidget)
        self.psnr_comp.setGeometry(QtCore.QRect(410, 380, 331, 300))
        self.psnr_comp.setText("")
        self.psnr_comp.setPixmap(QtGui.QPixmap("cuenca.png"))
        self.psnr_comp.setScaledContents(True)
        self.psnr_comp.setObjectName("psnr_comp")
        self.delay_comp = QtWidgets.QLabel(self.centralwidget)
        self.delay_comp.setGeometry(QtCore.QRect(410, 40, 331, 300))
        self.delay_comp.setText("")
        self.delay_comp.setPixmap(QtGui.QPixmap("cuenca.png"))
        self.delay_comp.setScaledContents(True)
        self.delay_comp.setObjectName("delay_comp")
        self.cpu_comp = QtWidgets.QLabel(self.centralwidget)
        self.cpu_comp.setGeometry(QtCore.QRect(770, 40, 331, 300))
        self.cpu_comp.setText("")
        self.cpu_comp.setPixmap(QtGui.QPixmap("cuenca.png"))
        self.cpu_comp.setScaledContents(True)
        self.cpu_comp.setObjectName("cpu_comp")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(560, 350, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.list_piso = QtWidgets.QListWidget(self.centralwidget)
        self.list_piso.setGeometry(QtCore.QRect(1120, 90, 41, 71))
        self.list_piso.setObjectName("list_piso")
        item = QtWidgets.QListWidgetItem()
        self.list_piso.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_piso.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_piso.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_piso.addItem(item)
        self.Btn_plot = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_plot.setGeometry(QtCore.QRect(1170, 100, 91, 31))
        self.Btn_plot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_plot.setMouseTracking(False)
        self.Btn_plot.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.Btn_plot.setObjectName("Btn_plot")
        self.Btn_plot.clicked.connect(self.plot)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1120, 70, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1120, 10, 131, 17))
        self.label_2.setObjectName("label_2")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(840, 350, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.time_comp = QtWidgets.QLabel(self.centralwidget)
        self.time_comp.setGeometry(QtCore.QRect(770, 380, 331, 300))
        self.time_comp.setText("")
        self.time_comp.setPixmap(QtGui.QPixmap("cuenca.png"))
        self.time_comp.setScaledContents(True)
        self.time_comp.setObjectName("time_comp")
        self.inputFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.inputFileButton.setGeometry(QtCore.QRect(1260, 10, 21, 25))
        self.inputFileButton.setObjectName("inputFileButton")
        self.inputFileButton.clicked.connect(self.onInputFileButtonClicked)
        self.inputFileLineEdit = QtWidgets.QLabel(self.centralwidget)
        self.inputFileLineEdit.setGeometry(QtCore.QRect(1120, 40, 181, 17))
        self.inputFileLineEdit.setObjectName("inputFileLineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1120, 170, 201, 17))
        self.label_3.setObjectName("label_3")
        self.select_tool = QtWidgets.QListWidget(self.centralwidget)
        self.select_tool.setGeometry(QtCore.QRect(1120, 190, 91, 41))
        self.select_tool.setObjectName("select_tool")
        item = QtWidgets.QListWidgetItem()
        self.select_tool.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.select_tool.addItem(item)
        self.time_comp.raise_()
        self.pl_comp.raise_()
        self.label_13.raise_()
        self.label_12.raise_()
        self.label_11.raise_()
        self.thr_comp.raise_()
        self.label_15.raise_()
        self.psnr_comp.raise_()
        self.delay_comp.raise_()
        self.cpu_comp.raise_()
        self.label_14.raise_()
        self.list_piso.raise_()
        self.Btn_plot.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.inputFileButton.raise_()
        self.inputFileLineEdit.raise_()
        self.label_16.raise_()
        self.label_3.raise_()
        self.select_tool.raise_()
        tercera.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(tercera)
        self.statusbar.setObjectName("statusbar")
        tercera.setStatusBar(self.statusbar)

        self.retranslateUi(tercera)
        QtCore.QMetaObject.connectSlotsByName(tercera)

    def retranslateUi(self, tercera):
        _translate = QtCore.QCoreApplication.translate
        tercera.setWindowTitle(_translate("tercera", "Graficas Comparativas"))
        self.label_13.setText(_translate("tercera", "Packet Loss"))
        self.label_12.setText(_translate("tercera", "Delay"))
        self.label_11.setText(_translate("tercera", "Throughput"))
        self.label_15.setText(_translate("tercera", "Uso de CPU"))
        self.label_14.setText(_translate("tercera", "PSNR"))
        __sortingEnabled = self.list_piso.isSortingEnabled()
        self.list_piso.setSortingEnabled(False)
        item = self.list_piso.item(0)
        item.setText(_translate("tercera", "1"))
        item = self.list_piso.item(1)
        item.setText(_translate("tercera", "3"))
        item = self.list_piso.item(2)
        item.setText(_translate("tercera", "5"))
        item = self.list_piso.item(3)
        item.setText(_translate("tercera", "7"))
        self.list_piso.setSortingEnabled(__sortingEnabled)
        self.Btn_plot.setText(_translate("tercera", "Graficar"))
        self.label.setText(_translate("tercera", "Piso:"))
        self.label_2.setText(_translate("tercera", "Seleccionar Video:"))
        self.label_16.setText(_translate("tercera", "Tiempo de Codificación"))
        self.inputFileButton.setText(_translate("tercera", "..."))
        self.inputFileLineEdit.setText(_translate("tercera", "-"))
        self.label_3.setText(_translate("tercera", "Seleccionar Herramienta Tx:"))
        __sortingEnabled = self.select_tool.isSortingEnabled()
        self.select_tool.setSortingEnabled(False)
        item = self.select_tool.item(0)
        item.setText(_translate("tercera", "GStreamer"))
        item = self.select_tool.item(1)
        item.setText(_translate("tercera", "FFMPEG"))
        self.select_tool.setSortingEnabled(__sortingEnabled)

    def plot(self):
        global bitrate, gop, fps, flag
        os.chdir('/media/christian/CPQR/Tesis/GUI/')
        conf_file = "tesis.conf"
        file = open(conf_file)
        config = file.readlines()
        bitrate = config[0]
        bitrate = bitrate[8:len(bitrate)-1]
        gop = config[1]
        gop = gop[4:len(gop)-1]
        fps = config[2]
        fps = fps[4:len(fps)-1]
        flag = self.select_tool.currentItem().text()
        if flag=='GStreamer':
            flag=0
        else:
            flag=1

        piso = self.list_piso.currentItem().text()

        os.chdir('/media/christian/CPQR/Tesis/GUI/Herramienta/rx')
        subprocess.run(['python3','grafica_prom_thro.py',str(video),str(piso), str(bitrate), str(gop), str(fps),str(flag)])
        os.chdir('/media/christian/CPQR/Tesis/GUI/Herramienta/metricas/delay')
        subprocess.run(['python3','plot_prom_delay.py',str(video),str(piso),str(flag)])
        os.chdir('/media/christian/CPQR/Tesis/GUI/Herramienta/metricas/PL')
        subprocess.run(['python3','plot_prom_PL.py',str(video),str(piso),str(flag)])
        os.chdir('/media/christian/CPQR/Tesis/GUI/Herramienta/tx')
        subprocess.run(['python3','cpu_prom_comp.py',str(video),str(piso), str(flag)])
        os.chdir('/media/christian/CPQR/Tesis/GUI/Herramienta/PSNR')
        subprocess.run(['./psnr.sh',str(video),str(piso), str(bitrate), str(gop), str(fps), str(flag)])
        subprocess.run(['python3','psnr.py',str(video),str(piso), str(bitrate), str(gop), str(fps), str(flag)])
        os.chdir('/media/christian/CPQR/Tesis/GUI/Herramienta/time_tx')
        subprocess.run(['python3','time_prom_comp.py',str(video),str(piso), str(flag)])
        if flag==0:
            self.pl_comp.setPixmap(QtGui.QPixmap('/media/christian/CPQR/Tesis/GUI/Herramienta/metricas/PL/PL_'+str(video)+"_piso"+str(piso)+"_PROM.png"))
            self.thr_comp.setPixmap(QtGui.QPixmap('/media/christian/CPQR/Tesis/GUI/Herramienta/rx/csv_through/figuras/throu_'+str(video)+"_piso"+str(piso)+"_PROM.png"))
            self.delay_comp.setPixmap(QtGui.QPixmap('/media/christian/CPQR/Tesis/GUI/Herramienta/metricas/delay/delay_'+str(video)+"_piso"+str(piso)+"_PROM.png"))
            self.psnr_comp.setPixmap(QtGui.QPixmap("/media/christian/CPQR/Tesis/GUI/Herramienta/PSNR/figuras_psnr/psnr_"+str(video)+"_piso"+piso+".png"))
            self.cpu_comp.setPixmap(QtGui.QPixmap("/media/christian/CPQR/Tesis/GUI/Herramienta/tx/figuras_cpu_comp/cpu_"+str(video)+"_piso"+piso+"_PROM.png"))
            self.time_comp.setPixmap(QtGui.QPixmap("/media/christian/CPQR/Tesis/GUI/Herramienta/time_tx/figuras_time/"+video+"_"+piso+"_PROM.png"))
        else:
            self.pl_comp.setPixmap(QtGui.QPixmap('/media/christian/CPQR/Tesis/GUI/Herramienta/metricas/PL_ffmpeg/PL_'+str(video)+"_piso"+str(piso)+"_PROM.png"))
            self.thr_comp.setPixmap(QtGui.QPixmap('/media/christian/CPQR/Tesis/GUI/Herramienta/rx/csv_through_ffmpeg/figuras/throu_'+str(video)+"_piso"+str(piso)+"_PROM.png"))
            self.delay_comp.setPixmap(QtGui.QPixmap('/media/christian/CPQR/Tesis/GUI/Herramienta/metricas/delay_ffmpeg/delay_'+str(video)+"_piso"+str(piso)+"_PROM.png"))
            self.psnr_comp.setPixmap(QtGui.QPixmap("/media/christian/CPQR/Tesis/GUI/Herramienta/PSNR/figuras_psnr_ffmpeg/psnr_"+str(video)+"_piso"+piso+".png"))
            self.cpu_comp.setPixmap(QtGui.QPixmap("/media/christian/CPQR/Tesis/GUI/Herramienta/tx/figuras_cpu_comp_ffmpeg/cpu_"+str(video)+"_piso"+piso+"_PROM.png"))
            self.time_comp.setPixmap(QtGui.QPixmap("/media/christian/CPQR/Tesis/GUI/Herramienta/time_tx_ffmpeg/figuras_time_ffmpeg/"+video+"_"+piso+"_PROM.png"))

    def onInputFileButtonClicked(self):
        global video, path
        file_filter = '*.yuv'
        filename = QFileDialog.getOpenFileNames(
            caption='Select a video file',
            directory=os.chdir("/media/christian/CPQR/Tesis"),
            filter=file_filter
        )
        if filename:
            video_arch = [tup[0] for tup in filename]
            video_arch1 = video_arch[0] 
            rep = video_arch1.count('/')
            pos1=0
            for x in range(0,rep):
                pos = video_arch1.find('/',pos1)
                pos1 = pos+1
            video = video_arch1[pos+1:len(video_arch1)-4]
            path = video_arch1[0:pos+1]
            self.inputFileLineEdit.setText(video)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tercera = QtWidgets.QMainWindow()
    ui = Ui_tercera()
    ui.setupUi(tercera)
    tercera.show()
    sys.exit(app.exec_())

