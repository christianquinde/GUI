#!/bin/bash
SELF_PATH=$1
bitrate=$2
bitrate=$(echo $bitrate | sed 's/.$//')
gop=$3
fps=$4
video=$5
SELF_PATH="$SELF_PATH${video}.yuv"

gst-launch-1.0 filesrc location=$SELF_PATH \
	! rawvideoparse format=2 width=352 height=288 \
	! videoconvert \
	! videorate \
	! video/x-raw, framerate="${fps}/1" \
	! x265enc bitrate=${bitrate} key-int-max=$gop \
	! queue \
	! filesink location=video/${video}_h265_${bitrate}k_${fps}_${gop}.mp4