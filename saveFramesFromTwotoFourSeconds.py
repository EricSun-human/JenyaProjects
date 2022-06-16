import cv2
import math
import os
videoFile = cv2.VideoCapture("C:\\Users\\Eric Sun\\Desktop\\RickRoll.mp4")

fps=videoFile.get(cv2.CAP_PROP_FPS)
#print(fps)

vidLen = int(videoFile.get(cv2.CAP_PROP_FRAME_COUNT))
#print(vidLen)

lastFrameToInclude=math.ceil(fps*4)
#print(minVideoLen)

try:
    if not os.path.exists("C:\\Users\\Eric Sun\\Desktop\\rangeOfVideoImgs"):
        os.makedirs("C:\\Users\\Eric Sun\\Desktop\\rangeOfVideoImgs")
except OSError:
    print("Error creating folder to contain the frames")

if vidLen<lastFrameToInclude:
    print("Video is to short to get frames from 2-4 seconds")
else:
    print("Starting to write frames...")
    frameNum=1
    #Gets the first and last frame starting at 2 and 6 seconds into the video
    firstFrameToInclude=math.ceil(fps*2)

    while(videoFile.isOpened()):
        ret, frame = videoFile.read()

        if ret==False:
            break

        if frameNum>=firstFrameToInclude and frameNum<=lastFrameToInclude:
            print("Writing Frame Num: "+str(frameNum))
            cv2.imwrite("C:\\Users\\Eric Sun\\Desktop\\rangeOfVideoImgs\\frame"+str(frameNum)+".jpg",frame)
        frameNum+=1
    #cv2.imwrite("C:\\Users\\Eric Sun\\Desktop\\"+str(frameNum)+".jpg",frame)
