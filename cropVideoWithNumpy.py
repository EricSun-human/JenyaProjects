import numpy as np
import cv2
from PIL import Image
import math
video = cv2.VideoCapture("C:\\Users\\erics\\OneDrive\\Desktop\\RickRoll.mp4")
numFrames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
croppedFrameWidth=math.floor(frameWidth/2)
croppedFrameHeight=math.floor(frameHeight/2)
fps = math.floor(video.get(cv2.CAP_PROP_FPS))
print(fps)
fourcc = cv2.VideoWriter_fourcc(*'X264')
croppedVideo=cv2.VideoWriter("C:\\Users\\erics\\OneDrive\\Desktop\\croppedVideo.mp4",fourcc,15,(frameWidth,frameHeight))

croppedFrames=[]
while(video.isOpened()):
    ret, frame = video.read()
    if ret==False:
        break
    #print(len(frame[0]))
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #print(type(frame))
    print(frame.shape)
    frame = frame[0:croppedFrameHeight,0:croppedFrameWidth]
    #print(len(frame[0]))
    #croppedFrame = Image.fromarray(frame)
    croppedVideo.write(frame)
    #icc = frame.info.get('icc_profile', '')
    #print(icc)
    #cv2.imwrite("C:\\Users\\erics\\OneDrive\\Desktop\\newFolder\\image.jpg",frame)

#for frame in croppedFrames:
video.release()
croppedVideo.release()
