import cv2

print("Information:")
video=cv2.VideoCapture("C:\\Users\\erics\\OneDrive\\Desktop\\RickRoll.mp4")

#Print out Dimensions
print("Height: "+str(video.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("Width: "+str(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

fps= int(video.get(cv2.CAP_PROP_FPS))

print("FPS: "+str(fps))
