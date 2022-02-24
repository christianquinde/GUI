#!/bin/bash
video=$1
delay=$2
pl=$3
codec=$4
piso=$5
flag=$6
sim=$7

if [[ flag -eq '0' ]]; then
	echo -e "$delay" > "Herramienta/metricas/delay/${video}_${codec}_piso${piso}_sim${sim}.csv"
	echo -e "$pl" > "Herramienta/metricas/PL/${video}_${codec}_piso${piso}_sim${sim}.csv"
else
	echo -e "$delay" > "Herramienta/metricas/delay_ffmpeg/${video}_${codec}_piso${piso}_sim${sim}.csv"
	echo -e "$pl" > "Herramienta/metricas/PL_ffmpeg/${video}_${codec}_piso${piso}_sim${sim}.csv"
fi
