#!/bin/bash
SELF_PATH=$1
bitrate=$2
gop=$3
fps=$4
video=$5
SELF_PATH="$SELF_PATH${video}.yuv"

ffmpeg \
    -s cif \
    -i $SELF_PATH \
    -an \
    -c:v libx264 \
    -b:v $bitrate \
    -g $gop \
    -r $fps \
    video_ffmpeg/${video}_h264_${bitrate}_${fps}_${gop}.mp4