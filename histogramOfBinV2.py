import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter
import numpy as np

def main(binFilePath,wantToSee,graphName):
    with open(binFilePath,'rb') as f:
        output_file = f.read()
    output_file=get_data_from_annotation_array(270, 480,output_file)
    numFrames = output_file.shape[2]
    #Valid input for wantToSee, which says what data histogram should plot
    if(type(wantToSee)==str and wantToSee=="all" or type(wantToSee)==int and wantToSee>0 and wantToSee<=numFrames):
        print("The program will now plot the histogram data.")
        fig = plt.figure(figsize=(8,8))
        if wantToSee=="all":
            output_file_reshaped=np.reshape(output_file,(270*numFrames,480))
            plt.hist(output_file_reshaped)
        else:
            plt.hist(output_file[wantToSee])
        plt.title("Histogram For Annotation Map Data(Frame: "+str(wantToSee)+")")
        plt.xlabel(".Bin File Values")
        plt.ylabel("Frequency")
        plt.savefig(graphName)
        plt.show()
    #Invalid input for wantToSee
    else:
        raise ValueError("Histogram Input Invalid. To see overall histogram, argument=all. Else, argument must be frame # int between 1 and "+str(numFrames)+".")
        print("Histogram Input Invalid. To see overall histogram, argument=all. Else, argument must be frame # int between 1 and "+str(numFrames)+".")
    

def get_data_from_annotation_array(height, width, annotation_buffer):
    '''returns array with dims: height, width, numFrames'''
    annotation = np.frombuffer(annotation_buffer, dtype=np.uint8) # Get error on this line-->TypeError: memoryview: a bytes-like object is required, not '_io.BufferedReader'
    annotation_np = annotation.reshape(width, height, -1, order='F').swapaxes(0, 1)
    return annotation_np.astype(np.uint8)#do 8bit unsigned int, try numpy and regular   

#To run this code on another computer, just add the correct path to the .bin file for binFilePath
binFilePath="C:\\Users\\erics\\Downloads\\jenya_4b3962e8-faba-4535-9c35-b3df955f2c9e_5_x264.bin"
#use argpars
wantToSee="all"#either frame num or string "all"
graphName="C:\\Users\\erics\\OneDrive\\Desktop\\graph.png"

main(binFilePath,wantToSee,graphName)


