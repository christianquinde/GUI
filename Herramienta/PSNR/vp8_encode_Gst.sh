#!/bin/bash
SELF_PATH=$1
bitrate=$2
rate=$bitrate
fac=1000
bitrate=$(echo $bitrate | sed 's/.$//') 
bitrate=$(($bitrate*$fac))
gop=$3
fps=$4
video=$5
SELF_PATH="$SELF_PATH${video}.yuv"

gst-launch-1.0 filesrc location=$SELF_PATH \
	! rawvideoparse format=2 width=352 height=288 \
	! videoconvert \
	! videorate \
	! video/x-raw, framerate="${fps}/1" \
	! vp8enc target-bitrate=${bitrate} keyframe-max-dist=$gop cpu-used=8 deadline=1 \
	! queue ! webmmux \
	! filesink location=video/${video}_VP8_${rate}_${fps}_${gop}.webm

