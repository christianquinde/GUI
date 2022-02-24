#!/bin/bash
video=$1
codec=$2
piso=$3
rate=$4
fps=$6
gop=$5
flag=$7
sim=$8


if [[ $flag -eq '0' ]]; then
	killall tcpdump
	echo "Conviertiendo a .csv ......."
	sleep 4
	./csv_convert.sh $flag
	mv trafico_tx.pcap pcaps/${video}_${codec}_${rate}_${fps}_${gop}_piso${piso}_sim${sim}.pcap
	mv trafico_tx_total.pcap pcaps_total/total_${video}_${codec}_${rate}_${fps}_${gop}_piso${piso}_sim${sim}.pcap
	mv trafico_tx.csv csv/${video}_${codec}_${rate}_${fps}_${gop}_piso${piso}_sim${sim}.csv
	mv trafico_tx_total.csv csv_total/total_${video}_${codec}_${rate}_${fps}_${gop}_piso${piso}_sim${sim}.csv
	echo "Conversion Finalizada ......."
else
	killall tcpdump
	echo "Conviertiendo a .csv ......."
	sleep 4
	./csv_convert.sh $flag
	mv trafico_tx.pcap pcaps_ffmpeg/${video}_${codec}_${rate}_${fps}_${gop}_piso${piso}_sim${sim}.pcap
	mv trafico_tx_total.pcap pcaps_total_ffmpeg/total_${video}_${codec}_${rate}_${fps}_${gop}_piso${piso}_sim${sim}.pcap
	mv trafico_tx.csv csv_ffmpeg/${video}_${codec}_${rate}_${fps}_${gop}_piso${piso}_sim${sim}.csv
	mv trafico_tx_total.csv csv_total_ffmpeg/total_${video}_${codec}_${rate}_${fps}_${gop}_piso${piso}_sim${sim}.csv
	echo "Conversion Finalizada ......."
fi
	
echo "--------------------------------FIN DE LA CONVERSION-----------------------------------"