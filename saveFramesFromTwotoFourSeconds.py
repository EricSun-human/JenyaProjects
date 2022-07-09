#"C:\Users\erics\OneDrive\Desktop\videoFrames"
import cv2
import numpy as np
import glob
from array import array

img_array = []
numImg=0
for filename in glob.glob("C:\\Users\\erics\\OneDrive\\Desktop\Animation_1080P-01b3\\Animation_1080P-01b3\*.png"):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    numImg+=1
print("Number of Images:"+str(numImg))

output_file = open('C:\\Users\\erics\\OneDrive\\Desktop\\{}_1280x720_yuv420p.yuv', 'wb')
for i in range(0,len(img_array),3):
    uElement=img_array[i]
    vElement=img_array[i+1]
    yElement=img_array[i+2]
    yElement.tofile(output_file)
    uElement.tofile(output_file)
    vElement.tofile(output_file)
output_file.close()

#use this format: {}_800x450_yuv420p.yuv + use y dimensions
