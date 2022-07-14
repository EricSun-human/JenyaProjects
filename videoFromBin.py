import numpy as np
import cv2
def get_data_from_annotation_array(height, width, annotation_buffer):
    '''returns array with dims: height, width, numFrames'''
    print("annotation_buffer type: "+str(type(annotation_buffer)))
    #print("annotation_buffer len: "+str(len(annotation_buffer)))
    print("annotation_buffer type"+str(type(annotation_buffer)))
    annotation = np.frombuffer(annotation_buffer, dtype=np.uint8) # Get error on this line-->TypeError: memoryview: a bytes-like object is required, not '_io.BufferedReader'
    annotation_np = annotation.reshape(width, height, -1, order='F').swapaxes(0, 1)
    return annotation_np.astype('float32')

#output_file = open("C:\\Users\\erics\\Downloads\\jenya_4b3962e8-faba-4535-9c35-b3df955f2c9e_5_x264.bin", 'rb')
with open("C:\\Users\\erics\\Downloads\\jenya_4b3962e8-faba-4535-9c35-b3df955f2c9e_5_x264.bin", 'rb') as f:
    output_file = f.read()
#print("output_file data:"+str(output_file))#Really Weird Issue: This print line causes Visual Studio to freeze up and stop responding
#for line in output_file:
    #print("\n"+str(line))

redChannelArray = get_data_from_annotation_array(270, 480,output_file)
print(redChannelArray.shape)
height, width, numFrames = redChannelArray.shape
print(str(height)+"\n"+str(width)+"\n"+str(numFrames))
print(len(redChannelArray))

#This line creates an empty array for the G and B channels - note to self: may need to change type from int to float if rgb img no work
#greenChannelArray,blueChannelArray=np.zeros((270,480),np.int8),np.zeros((270,480),np.int8)
#greenChannelArray,blueChannelArray=np.zeros((height,width,numFrames),np.int8),np.zeros((height,width,numFrames),np.int8)#for int
greenChannelArray,blueChannelArray=np.zeros((height,width,numFrames),np.float64),np.zeros((height,width,numFrames),np.float64)#for float
print(greenChannelArray)
print(blueChannelArray)
print(greenChannelArray.shape)
print(blueChannelArray.shape)

#videoArray = cv2.merge([blueChannelArray,greenChannelArray,redChannelArray])# Merge B, G, R arrays into a video
#videoArray = cv2.merge([redChannelArray,blueChannelArray,greenChannelArray])#should be BGR i'm just debugging
#videoArray = np.stack(blueChannelArray,greenChannelArray,redChannelArray)# Merge B, G, R arrays into a video

fps=25#how to get actual fps?
out = cv2.VideoWriter("C:\\Users\\erics\\OneDrive\\Desktop\\annotationMapVideo.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width,height))#Stack Overflow says cv2 arguments for dimensions opposite of np, pass width then height
print("----Frame Data Here:----")
for i in range(numFrames):
    data=videoArray[i]
    print(data)
    out.write(data)
    print("wrote np data for frame #"+str(i))
out.release()

