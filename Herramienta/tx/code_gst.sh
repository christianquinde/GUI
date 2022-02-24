#!/bin/bash
#SELF_PATH="$PWD/video.mp4" \
SELF_PATH="/media/christian/CPQR/Tesis/metricas_finales/videos_codificados/foreman_cif_h264_250k_20_30.mp4" \
PEER_V=9004 PEER_IP=127.0.0.1 \
SELF_V=5004 SELF_VSSRC=112233 \
bash -c 'gst-launch-1.0 -e \
    uridecodebin uri="file://$SELF_PATH" \
        ! videoconvert ! x264enc bitrate=10 key-int-max=30 \
        ! filesink location=video_enc.mp4'
