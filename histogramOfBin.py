import matplotlib.pyplot as plt
import numpy as np

#To run this code on another computer, just add the correct path to the .bin file for binFilePath
binFilePath="C:\\Users\\erics\\Downloads\\jenya_4b3962e8-faba-4535-9c35-b3df955f2c9e_5_x264.bin"
numFrames=120#use argpars


#histogram()
#def histogram(binFilePath,numFrames):
#    blahblahblah

def get_data_from_annotation_array(height, width, annotation_buffer):
    '''returns array with dims: height, width, numFrames'''
    print("annotation_buffer type: "+str(type(annotation_buffer)))
    #print("annotation_buffer len: "+str(len(annotation_buffer)))
    print("annotation_buffer type"+str(type(annotation_buffer)))
    annotation = np.frombuffer(annotation_buffer, dtype=np.uint8) # Get error on this line-->TypeError: memoryview: a bytes-like object is required, not '_io.BufferedReader'
    annotation_np = annotation.reshape(width, height, -1, order='F').swapaxes(0, 1)
    return annotation_np.astype(np.uint8)#do 8bit unsigned int, try numpy and regular

#with open("C:\\Users\\erics\\Downloads\\jenya_4b3962e8-faba-4535-9c35-b3df955f2c9e_5_x264.bin",encoding='ANSI') as f:
#    output_file = f.read()

with open(binFilePath,'rb') as f:
    output_file = f.read()

print("started output file conversion to array")
output_file=get_data_from_annotation_array(270, 480,output_file)
#output_file=np.array(output_file)
testData = np.random.normal(170, 10, 250)
print("finished output file conversion to array")
print(type(output_file))

print("The program will now cycle through each frame by plotting its data, then waiting 10 seconds, then plotting data of the next frame.")
for i in range(numFrames):
    fig = plt.figure(figsize=(10,10))
    ax = fig.gca()
    ax.set_aspect("equal")
    plt.hist(output_file[i],bins=256)
    plt.title("Histogram For Annotation Map Data(Frame #"+str(i+1)+")")
    plt.xlabel(".Bin File Values")
    plt.ylabel("Frequency")
    plt.show(block=False)
    plt.pause(10)
    plt.close()

   
