#!/bin/bash
video=$1
codec=$2
piso=$3
bitrate=$4
gop=$5
fps=$6
flag=$7
sim=$8

if [[ $flag -eq '0' ]]; then
	netcat -l 9899 | pv > info_delay.csv
	mv info_delay.csv Herramienta/rx/csv/${video}_${codec}_${bitrate}_${fps}_${gop}_piso${piso}_sim${sim}.csv

	netcat -l 9998 | pv > info_packet_loss.csv
	mv info_packet_loss.csv Herramienta/rx/csv_total/total_${video}_${codec}_${bitrate}_${fps}_${gop}_piso${piso}_sim${sim}.csv

	netcat -l 9989 | pv > info_throughput.csv
	mv info_throughput.csv Herramienta/rx/csv_through/through_${video}_${codec}_${bitrate}_${fps}_${gop}_piso${piso}_sim${sim}.csv
else
	netcat -l 9899 | pv > info_delay.csv
	mv info_delay.csv Herramienta/rx/csv_ffmpeg/${video}_${codec}_${bitrate}_${fps}_${gop}_piso${piso}_sim${sim}.csv

	netcat -l 9998 | pv > info_packet_loss.csv
	mv info_packet_loss.csv Herramienta/rx/csv_total_ffmpeg/total_${video}_${codec}_${bitrate}_${fps}_${gop}_piso${piso}_sim${sim}.csv

	netcat -l 9989 | pv > info_throughput.csv
	mv info_throughput.csv Herramienta/rx/csv_through_ffmpeg/through_${video}_${codec}_${bitrate}_${fps}_${gop}_piso${piso}_sim${sim}.csv
fi
