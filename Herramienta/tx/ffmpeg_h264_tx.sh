#!/bin/bash
PEER_V=$1
PEER_IP=$2 
SELF_PATH=$3
bitrate=$4
gop=$5
fps=$6

video=$7
codec=$8
piso=$9
sim=${10}

ffmpeg \
    -re \
    -fflags +genpts \
    -s cif \
    -i $SELF_PATH \
    -an \
    -c:v libx264 \
    -b:v $bitrate \
    -g $gop \
    -r $fps \
    -f rtp \
    -strict experimental \
    "rtp://${PEER_IP}:${PEER_V}" |& tee ../time_tx_ffmpeg/${video}_${codec}_piso${piso}_sim${sim}.txt