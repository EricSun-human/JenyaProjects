import numpy as np

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

videoArray = get_data_from_annotation_array(270, 480,output_file)
print(videoArray.shape)
height, width, numFrames = videoArray.shape
print(str(height)+"\n"+str(width)+"\n"+str(numFrames))
print(len(videoArray))

greenChannelArray,blueChannelArray=np.zeros((270,480),np.int8),np.zeros((270,480),np.int8)#note to self: may need to change type from int to float if rgb img no work
print(greenChannelArray)
print(blueChannelArray)
#for i in range(numFrames):
#    print(videoArray[;,i])
