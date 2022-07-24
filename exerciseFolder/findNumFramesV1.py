import cv2
danceVideo = cv2.VideoCapture("C:\\Users\\erics\\OneDrive\\Desktop\\RickRoll.mp4")
#counts the number of frames using cv2.CAP_PROP_FRAME_COUNT and then prints the number
lenVideo= danceVideo.get(cv2.CAP_PROP_FRAME_COUNT)
print("The number of frames is: "+str(lenVideo))
