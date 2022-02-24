#!/bin/bash
video=$1
codec=$2
bitrate=$3
gop=$4
fps=$5
flag=$6

if [[ $codec == 'h264' ]]; then
 
    ext='mp4'
elif [[ $codec == 'h265' ]]; then
 
    ext='mp4'
elif [[ $codec == 'VP8' ]]; then
 
    ext='webm'
elif [[ $codec == 'VP9' ]]; then
 
    ext='webm'
fi

ffplay ${video}_${codec}_${bitrate}_${fps}_${gop}.$ext