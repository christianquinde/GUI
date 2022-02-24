#!/bin/bash

SELF_VSSRC='112233'

video=$1
codec=$2
PEER_IP=$3
PEER_V=$4
ext=$5
piso=$6
SELF_PATH=$7
SELF_PATH="${SELF_PATH}${video}.yuv"

gop=$9
fps=${10}
bitrate=${8}

flag=${11}
sim=${12}

ip_src=${13}

if [[ $flag -eq '0' ]]; then
    gnome-terminal --title "Captura_Tx" -- ./trafico.sh $PEER_V $ip_src $PEER_IP
    echo "Enviando ${video}_${codec}_${bitrate}_${fps}_${gop}......" 
    sleep 2
    if [[ $codec == h264 ]]; then
        echo $codec
        ./cpu_usage.sh $video $codec $piso $flag $sim & 
        ./test_h264.sh $PEER_V $PEER_IP $SELF_PATH $video $codec $piso $bitrate $gop $fps $sim
        killall cpu_usage.sh
        killall top
    elif [[ $codec == h265 ]]; then
        echo $codec
        ./cpu_usage.sh $video $codec $piso $flag $sim &
        ./test_h265.sh $PEER_V $PEER_IP $SELF_PATH $video $codec $piso $bitrate $gop $fps $sim
        killall cpu_usage.sh
        killall top
    elif [[ $codec == VP8 ]]; then
        echo $codec
        ./cpu_usage.sh $video $codec $piso $flag $sim &
        ./test_vp8.sh $PEER_V $PEER_IP $SELF_PATH $video $codec $piso $bitrate $gop $fps $sim
        killall cpu_usage.sh
        killall top
    else
        echo $codec
        ./cpu_usage.sh $video $codec $piso $flag $sim &
        ./test_vp9.sh $PEER_V $PEER_IP $SELF_PATH $video $codec $piso $bitrate $gop $fps $sim
        killall cpu_usage.sh
        killall top
    fi
else
    gnome-terminal --title "Captura_Tx" -- ./trafico.sh $PEER_V $ip_src $PEER_IP
    echo "Enviando ${video}_${codec}_${bitrate}_${fps}_${gop}......" 
    sleep 2
    if [[ $codec == h264 ]]; then
        echo $codec
        ./cpu_usage.sh $video $codec $piso $flag $sim & 
        ./ffmpeg_h264_tx.sh $PEER_V $PEER_IP $SELF_PATH $bitrate $gop $fps $video $codec $piso $sim
        killall cpu_usage.sh
        killall top
    elif [[ $codec == h265 ]]; then
        echo $codec
        ./cpu_usage.sh $video $codec $piso $flag $sim & 
        ./ffmpeg_h265_tx.sh $PEER_V $PEER_IP $SELF_PATH $bitrate $gop $fps $video $codec $piso $sim
        killall cpu_usage.sh
        killall top
    elif [[ $codec == VP8 ]]; then
        echo $codec
        ./cpu_usage.sh $video $codec $piso $flag $sim &
        ./ffmpeg_vp8_tx.sh $PEER_V $PEER_IP $SELF_PATH $bitrate $gop $fps $video $codec $piso $sim
        killall cpu_usage.sh
        killall top
    else
        echo $codec
        ./cpu_usage.sh $video $codec $piso $flag $sim & 
        ./ffmpeg_vp9_tx.sh $PEER_V $PEER_IP $SELF_PATH $bitrate $gop $fps $video $codec $piso $sim
        killall cpu_usage.sh
        killall top
    fi
fi

 
echo "--------------------------------FIN DE LA TRANSMISION-----------------------------------"




