#!/bin/bash
flag=$1

if [[ $flag -eq '0' ]]; then
	cd Figs/Gst 
	cp -a ../../Herramienta/figuras_throu/*.png Through
	cp -a ../../Herramienta/tx/figuras_cpu/*.png CPU
echo "-------------- Figuras Ventana 1 Guardadas ----------------------"
	cp -a ../../Herramienta/metricas/PL/*.png PL_comp
	cp -a ../../Herramienta/rx/csv_through/figuras/*.png Through_comp
	cp -a ../../Herramienta/metricas/delay/*.png Delay_comp
	cp -a ../../Herramienta/PSNR/figuras_psnr/*.png PSNR
	cp -a ../../Herramienta/tx/figuras_cpu_comp/*.png CPU_comp
	cp -a ../../Herramienta/time_tx/figuras_time/*.png Time_comp
echo "-------------- Figuras Ventana 2 Guardadas ----------------------"
	mv PL_comp/*PROM.png PL_prom
	mv Through_comp/*PROM.png Through_prom
	mv Delay_comp/*PROM.png Delay_prom
	mv CPU_comp/*PROM.png CPU_prom
	mv Time_comp/*PROM.png Time_prom
echo "-------------- Figuras Ventana 3 Guardadas ----------------------"
else
	cd Figs/FFMPEG
	cp -a ../../Herramienta/figuras_throu_ffmpeg/*.png Through
	cp -a ../../Herramienta/tx/figuras_cpu_ffmpeg/*.png CPU
echo "-------------- Figuras Ventana 1 Guardadas ----------------------"
	cp -a ../../Herramienta/metricas/PL_ffmpeg/*.png PL_comp
	cp -a ../../Herramienta/rx/csv_through_ffmpeg/figuras/*.png Through_comp
	cp -a ../../Herramienta/metricas/delay_ffmpeg/*.png Delay_comp
	cp -a ../../Herramienta/PSNR/figuras_psnr_ffmpeg/*.png PSNR
	cp -a ../../Herramienta/tx/figuras_cpu_comp_ffmpeg/*.png CPU_comp
	cp -a ../../Herramienta/time_tx_ffmpeg/figuras_time_ffmpeg/*.png Time_comp
echo "-------------- Figuras Ventana 2 Guardadas ----------------------"
	mv PL_comp/*PROM.png PL_prom
	mv Through_comp/*PROM.png Through_prom
	mv Delay_comp/*PROM.png Delay_prom
	mv CPU_comp/*PROM.png CPU_prom
	mv Time_comp/*PROM.png Time_prom
echo "-------------- Figuras Ventana 3 Guardadas ----------------------"
fi
