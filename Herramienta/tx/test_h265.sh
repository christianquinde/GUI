#!/bin/bash
PEER_V=$1
PEER_IP=$2 
SELF_PATH=$3
SELF_VSSRC='112233'
video=$4
codec=$5
piso=$6
bitrate=$7
bitrate=$(echo $bitrate | sed 's/.$//') 
gop=$8
fps=$9
sim=${10}
gst-launch-1.0 -t \
    rtpsession name=r sdes="application/x-rtp-source-sdes,cname=(string)\"user\@example.com\"" \
    filesrc location=$SELF_PATH \
    ! rawvideoparse format=2 width=352 height=288 \
    ! videoconvert \
    ! videorate ! video/x-raw,framerate="${fps}/1" \
    ! x265enc bitrate=$bitrate key-int-max=$gop \
    ! rtph265pay \
    ! "application/x-rtp,payload=(int)103,clock-rate=(int)90000,ssrc=(uint)$SELF_VSSRC" \
    ! r.send_rtp_sink r.send_rtp_src \
    ! udpsink host=$PEER_IP port=$PEER_V udpsrc port=$((PEER_V+1)) \
    ! r.recv_rtcp_sink > ../time_tx/${video}_${codec}_piso${piso}_sim${sim}.txt
