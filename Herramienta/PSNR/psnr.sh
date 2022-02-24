#!/bin/bash

#declare -a video=("foreman_cif" "news_cif" "mother-daughter_cif")
#arraylength_video=${#video[@]}
video=$1
piso=$2
bitrate=$3
gop=$4
fps=$5
flag=$6

declare -a codecs=("h264" "h265" "vp8" "vp9")
#declare -a codecs=("libvpx" "libvpx-vp9")
arraylength_codecs=${#codecs[@]}

if [[ -f ${video}.y4m ]]; then
	echo "Archivo y4m Encontrado..."
else
	echo "Generando Archivo y4m..."
	ffmpeg -s cif -i ../../../${video}.yuv ${video}.y4m
fi


for (( j=0; j<${arraylength_codecs}; j++ ));
do
	if [[ flag -eq '0' ]]; then
	
		if [[ ${codecs[$j]} == "h264" ]]
		then
			ffmpeg -i ${video}.y4m -i video/${video}_h264_${bitrate}_${fps}_${gop}.mp4 -lavfi psnr="stats_file=psnr.log" -f null -
		    mv psnr.log logs/psnr_${video}_h264_${bitrate}_${fps}_${gop}_piso${piso}.log
		elif [[ ${codecs[$j]} == "vp8" ]]
		then
			ffmpeg -i ${video}.y4m -i video/${video}_VP8_${bitrate}_${fps}_${gop}.webm -lavfi psnr="stats_file=psnr.log" -f null -
		    mv psnr.log logs/psnr_${video}_VP8_${bitrate}_${fps}_${gop}_piso${piso}.log
		elif [[ ${codecs[$j]} == "vp9" ]]
		then
			ffmpeg -i ${video}.y4m -i video/${video}_VP9_${bitrate}_${fps}_${gop}.webm -lavfi psnr="stats_file=psnr.log" -f null -
		    mv psnr.log logs/psnr_${video}_VP9_${bitrate}_${fps}_${gop}_piso${piso}.log
		else
			ffmpeg -i ${video}.y4m -i video/${video}_h265_${bitrate}_${fps}_${gop}.mp4 -lavfi psnr="stats_file=psnr.log" -f null -
		    mv psnr.log logs/psnr_${video}_h265_${bitrate}_${fps}_${gop}_piso${piso}.log
		fi 
	else
		if [[ ${codecs[$j]} == "h264" ]]
		then
			ffmpeg -i ${video}.y4m -i video_ffmpeg/${video}_h264_${bitrate}_${fps}_${gop}.mp4 -lavfi psnr="stats_file=psnr.log" -f null -
		    mv psnr.log logs_ffmpeg/psnr_${video}_h264_${bitrate}_${fps}_${gop}_piso${piso}.log
		elif [[ ${codecs[$j]} == "vp8" ]]
		then
			ffmpeg -i ${video}.y4m -i video_ffmpeg/${video}_VP8_${bitrate}_${fps}_${gop}.webm -lavfi psnr="stats_file=psnr.log" -f null -
		    mv psnr.log logs_ffmpeg/psnr_${video}_VP8_${bitrate}_${fps}_${gop}_piso${piso}.log
		elif [[ ${codecs[$j]} == "vp9" ]]
		then
			ffmpeg -i ${video}.y4m -i video_ffmpeg/${video}_VP9_${bitrate}_${fps}_${gop}.webm -lavfi psnr="stats_file=psnr.log" -f null -
		    mv psnr.log logs_ffmpeg/psnr_${video}_VP9_${bitrate}_${fps}_${gop}_piso${piso}.log
		else
			ffmpeg -i ${video}.y4m -i video_ffmpeg/${video}_h265_${bitrate}_${fps}_${gop}.mp4 -lavfi psnr="stats_file=psnr.log" -f null -
		    mv psnr.log logs_ffmpeg/psnr_${video}_h265_${bitrate}_${fps}_${gop}_piso${piso}.log
		fi
	fi
done