#!/bin/bash
time=100
cont=1
video=$1
codec=$2
piso=$3
flag=$4
sim=$5

if [[ $flag -eq '0' ]]; then
	if [ -f CPU/cpu_usage_${video}_${codec}_piso${piso}_sim${sim}.txt ];
	then
	rm -R CPU/cpu_usage_${video}_${codec}_piso${piso}_sim${sim}.txt
	top -b > CPU/cpu_usage_${video}_${codec}_piso${piso}_sim${sim}.txt
	else
	top -b > CPU/cpu_usage_${video}_${codec}_piso${piso}_sim${sim}.txt
	fi
else
	if [ -f CPU_ffmpeg/cpu_usage_${video}_${codec}_piso${piso}_sim${sim}.txt ];
	then
	rm -R CPU_ffmpeg/cpu_usage_${video}_${codec}_piso${piso}_sim${sim}.txt
	top -b > CPU_ffmpeg/cpu_usage_${video}_${codec}_piso${piso}_sim${sim}.txt
	else
	top -b > CPU_ffmpeg/cpu_usage_${video}_${codec}_piso${piso}_sim${sim}.txt
	fi
fi




