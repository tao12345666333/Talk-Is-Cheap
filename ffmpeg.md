ffmpeg -i little-start1.mp3 -i gms1.mp3 -i za.mp3 -filter_complex '[0:0][1:0][2:0]concat=n=3:v=0:a=1[out]' -map '[out]' output.mp3

* 将视频转换为480X480,29.97fps,1200kbps,H.264编码的视频:

```
ffmpeg -i old.mp4 -r 29.97 -s 480×480 -b:v 1200k -acodec libfdk_aac -vcodec h264 -y new.mp4 ;
```

该行命令中参数 -r 指定帧率 , -s 指定尺寸 , -b:v 指定视频码率 , -acodec libfdk_aac 指定fdk_aac来编码音频 , -vcodec h264 指定用h264编码视频
