import cv2
import numpy as np
import os

#create 3 arrays for our colors(Ask Jenya how to initiate empty arrays properly)
# blueChannelArray = [0]*3
# redChannelArray = [0]*3
# greenChannelArray = [0]*3

videoFile=cv2.VideoCapture("C:\\Users\\Eric Sun\\Desktop\\RickRoll.mp4")
frameNum=1

#Creates a folder if not there already
for i in["blueChannel","greenChannel","redChannel"]:
    try:
        if not os.path.exists("C:\\Users\\Eric Sun\\Desktop\\RGBImages\\"+i):
            os.makedirs("C:\\Users\\Eric Sun\\Desktop\\RGBImages\\"+i)
    except OSError:
        print ('Error: Creating directory: '+i)

while(videoFile.isOpened() and frameNum<11):
    ret, frame = videoFile.read()


    if ret == False:
        print("End of video")
        break

    #split the image into its three channels
    B,G,R = cv2.split(frame)
    
    
    print("writing frame: "+str(frameNum))
    #cv2.imshow("Blue",B)
    #cv2.imshow("Green", G)
    #cv2.imshow("Red", R)

    cv2.imwrite("C:\\Users\\Eric Sun\\Desktop\\RGBImages\\blueChannel\\blueChannelFrame"+str(frameNum)+".jpg", B)
    cv2.imwrite("C:\\Users\\Eric Sun\\Desktop\\RGBImages\\greenChannel\\greenChannelFrame"+str(frameNum)+".jpg", G)
    cv2.imwrite("C:\\Users\\Eric Sun\\Desktop\\RGBImages\\redChannel\\redChannelFrame"+str(frameNum)+".jpg", R)
    #cv2.imwrite("D://medium_blogs//channel_green.jpg", G)
    #cv2.imwrite("D://medium_blogs//channel_blue.jpg", B)
    frameNum+=1





