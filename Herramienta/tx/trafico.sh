#!/bin/bash
rtpport=$1
ip_src=$2
ip_dst=$3
rtcpport=$((rtpport+1))

#tcpdump port $rtpport and udp and src $ip_src and dst $ip_dst -w trafico_tx_total.pcap -i tun0 &
#tcpdump port $rtcpport and src $ip_dst -w trafico_tx.pcap -i tun0 
tcpdump port $rtpport and udp and src $ip_src and dst $ip_dst -w trafico_tx_total.pcap -i wlx00c0ca5a278a &
tcpdump port $rtcpport and src $ip_dst -w trafico_tx.pcap -i wlx00c0ca5a278a 
#tcpdump port $rtpport and udp and src $ip_src and dst $ip_dst -w trafico_tx_total.pcap -i lo &
#tcpdump port $rtcpport and src $ip_dst -w trafico_tx.pcap -i lo 
#sleep 15
#killall tcpdump 
