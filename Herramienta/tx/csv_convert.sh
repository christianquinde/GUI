#!/bin/bash
flag=$1
if [[ $flag -eq '0' ]]; then
	tshark -r trafico_tx.pcap -T fields -e frame.time > trafico_tx.csv
	tshark -r trafico_tx_total.pcap -T fields -e frame.time > trafico_tx_total.csv	
else
	tshark -r trafico_tx.pcap -T fields -e frame.time > trafico_tx.csv
	tshark -r trafico_tx_total.pcap -T fields -e frame.time > trafico_tx_total.csv
fi

