#"C:\Users\erics\OneDrive\Desktop\videoFrames"
import numpy as np
import glob
from array import array
import cv2
import time
from PIL import Image
img_array = []
numImg=0
for filename in glob.glob("C:\\Users\\erics\\OneDrive\\Desktop\\HowTo_720P-017a\\*.png"):
    print("filename: "+str(filename))
    img = np.array(Image.open(str(filename)))#cv2.imread(filename)Image.fromarray(videoArray[0])
    height, width = img.shape
    print(img.shape)
    #print("layers: "+str(layers))# This should be one since it should already be split into Y U V layers, but It's saying each thing has three layers
    size = (width,height)
    img_array.append(img)
    numImg+=1
print("Number of Images:"+str(numImg))

#output_file = open('C:\\Users\\erics\\OneDrive\\Desktop\\{}_1280x720_yuv420p.yuv', 'w')
#output_file = open('C:\\Users\\erics\\OneDrive\\Desktop\\{}_1280x720_yuv420p.yuv', 'wb')
#print(output_file)

with open("C:\\Users\\erics\\OneDrive\\Desktop\\howto_1280x720_yuv420p.yuv", 'wb') as output_file:#use format(https://www.w3schools.com/python/ref_string_format.asp) for .yuv file name
    for i in range(0,len(img_array),3):
        uElement=img_array[i]
        vElement=img_array[i+1]
        yElement=img_array[i+2]
        #print("uElement"+str(uElement))
        #print("vElement"+str(vElement))
        #print("yElement"+str(yElement))
        #output_file.write(yElement)#doesn't work since its a numpy array. Says: write() argument must be str, not numpy.ndarray
        #output_file.write(uElement)
        #output_file.write(vElement)
        output_file.write(yElement)#doesn't work since its a numpy array. Says: write() argument must be str, not numpy.ndarray
        output_file.write(uElement)
        output_file.write(vElement)
        #yElement.tofile(output_file)
        #uElement.tofile(output_file)
        #vElement.tofile(output_file)
        #time.sleep(2)
#output_file.close()

#use this format: {}_800x450_yuv420p.yuv + use y dimensions
