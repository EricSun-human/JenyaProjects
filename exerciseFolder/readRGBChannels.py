import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

#create 3 arrays for our colors(Ask Jenya how to initiate empty arrays properly)
# blueChannelArray = [0]*3
# redChannelArray = [0]*3
# greenChannelArray = [0]*3

videoFile=cv2.VideoCapture("C:\\Users\\Eric Sun\\Desktop\\RickRoll.mp4")
i=0
R_frames = []
G_frames = []
B_frames = []

n_bins = 200


while(videoFile.isOpened()):
    ret, frame = videoFile.read()

    #If a frame is missing
    if ret == False:
        print("End of video")
        break

    #split the image into its three channels
    B,G,R = cv2.split(frame)
    cv2.imshow('frame', B)
    # print(B.shape)
    # print(B)
    #print(frame)

    B_frames.append(B)
    G_frames.append(G)
    R_frames.append(R)

    #while (1):
    #    if cv2.waitKey(1) == ord('n'):
    #        break
    #continue

B_movie = np.asarray(B_frames)
G_movie = np.asarray(G_frames)
R_movie = np.asarray(R_frames)


# print(B_movie)

n_bins = 200
# Creating histogram
fig, axs = plt.subplots(1, 3)

#This line didn't end up working :(
plt.title('RGB Value Histogram')

print(B_movie.flatten())
axs[0].set_title("R movie histogram")
axs[0].hist(R_movie.flatten(), bins = n_bins, color='r')
axs[1].set_title("G movie histogram")
axs[1].hist(G_movie.flatten(), bins = n_bins, color='g')
axs[2].set_title("B movie histogram")
axs[2].hist(B_movie.flatten(), bins = n_bins, color='b')
 
# Show plot
plt.show()

while (1):
    if cv2.waitKey(1) == ord('q'):
        break
