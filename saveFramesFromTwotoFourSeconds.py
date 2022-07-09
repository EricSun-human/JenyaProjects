import ffmpeg
#import cv2
#import subprocess as sp
import os
os.system("ffmpeg -i rickroll.mp4 -ss 00:00:02 -t 00:00:02 -async 1 -strict -2 cutRickRoll.mp4")
os.system("cd cutRickroll")
os.system("ffmpeg -i cutRickRoll.mp4 -r 24/1 out%03d.jpg")
