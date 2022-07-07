import ffmpeg
#import cv2
#import subprocess as sp
import os
os.system("ffmpeg -i rickroll.mp4 -ss 00:00:02 -t 00:00:02 -async 1 -strict -2 cutRickRoll.mp4")
os.system("cd cutRickroll")
os.system("ffmpeg -i cutRickRoll.mp4 -r 24/1 out%03d.jpg")
# video = cv2.VideoCapture("C:\\Users\\erics\\OneDrive\\Desktop\\RickRoll.mp4")

#audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
#video = input.video.hflip()
#out = ffmpeg.output(audio, video, 'out.mp4')

#probe = ffmpeg.probe("C:\\Users\\erics\\OneDrive\\Desktop\\RickRoll.mp4")
#FFMPEG_BIN = "ffmpeg.exe" # on Windows
#command = [ FFMPEG_BIN,'-i', 'RickRoll.mp4','-f', 'image2pipe','-pix_fmt', 'rgb24','-vcodec', 'rawvideo', '-']
#pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)

#video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
#fps = int(video_info['r_frame_rate'].split('/')[0])

#stream = ffmpeg.input('C:\\Users\\erics\\OneDrive\\Desktop\\RickRoll.mp4')
#stream = ffmpeg.hflip(stream)
#stream = ffmpeg.output(stream, 'C:\\Users\\erics\\OneDrive\\Desktop\\output.mp4')
#ffmpeg.run(stream)

#probe = ffmpeg.probe('C:\\Users\\erics\\OneDrive\\Desktop\\RickRoll.mp4')
#video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
#fps = int(video_info['r_frame_rate'].split('/')[0])
#print("fps: "+str(fps))
#input = ffmpeg.input('RickRoll.mp4')
#audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
#video = input.video.hflip()
#out = ffmpeg.output(audio, video, 'out.mp4')
