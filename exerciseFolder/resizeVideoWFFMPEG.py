import os
import ffmpeg
#I ended up just doing this through the command prompt, this file just has the lines to enter(cd.. didn't work in the VE)
#Get to desktop
for i in range(3):
    os.system("cd..")
os.system("chdir")
#video dims: 916 x 720
os.system("cd Onedrive")
os.system("cd desktop")

os.system("ffmpeg -i RickRoll.mp4 -vf scale=458:-1 C:\\Users\\erics\\OneDrive\\Desktop\\croppedRickroll.mp4")
os.system("ffmpeg -i RickRoll.mp4 -vf scale=-1:360 C:\\Users\\erics\\OneDrive\\Desktop\\croppedRickroll.mp4")
