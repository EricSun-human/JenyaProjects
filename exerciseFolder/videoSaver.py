import cv2
import os
import pandas as pd
#opens my rickroll video
videoFile = cv2.VideoCapture("C:\\Users\\erics\\OneDrive\\Desktop\\RickRoll.mp4")
i=0

while(videoFile.isOpened()):
    #ret: a bool that returns true if there is more frames dans notre video
    #frame:gets frame
    ret, frame = videoFile.read()

    #is this necessary?
    if ret == False:
        break

    cv2.imwrite('C:\\Users\\erics\\OneDrive\\Desktop\\videoFrames\\rickrollframe'+str(i)+'.jpg',frame)
    i+=1

videoFile.release()
cv2.destroyAllWindows()
