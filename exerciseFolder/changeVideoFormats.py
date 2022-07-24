import os
os.system("cd OneDrive")
os.system("cd Desktop")
os.system("ffmpeg -i RickRoll.mp4 -c:v rawvideo convertedToRAW.raw"
#Converts w/out raising error, but yuv files are not openable w/ YUV reader
os.system("ffmpeg -i RickRoll.mp4 -c:v rawvideo convertedToRAW.yuv"))
os.system("ffmpeg -i RickRoll.mp4 convertedToRAW.yuv")
