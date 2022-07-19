import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter
import numpy as np
import argparse

def main(height,width,binFilePath,wantToSee,graphName):
    with open(binFilePath,'rb') as f:
        output_file = f.read()
    output_file=get_data_from_annotation_array(height, width,output_file)
    numFrames = output_file.shape[2]
    #Valid input for wantToSee, which says what data histogram should plot(i.e. histogram for frame #2)
    if(type(wantToSee)==str and wantToSee=="all" or type(wantToSee)==int and wantToSee>0 and wantToSee<=numFrames):
        print("The program will now plot the histogram data.")
        fig = plt.figure(figsize=(8,8))
        if wantToSee=="all":
            output_file_reshaped=np.reshape(output_file,(height*numFrames*width,1))
            plt.hist(output_file_reshaped,bins=256)
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

#Implimentation w/out argpars
binFilePath="C:\\Users\\erics\\Downloads\\jenya_4b3962e8-faba-4535-9c35-b3df955f2c9e_5_x264.bin"#add the correct path to the .bin file for binFilePath
wantToSee="all"#Histogram will be shown for this data. Either enter a frame number or "all" to see histogram for overall
graphName="C:\\Users\\erics\\OneDrive\\Desktop\\graph.png"#enter path for picture of graph created
height=270
width=480
main(height,width,binFilePath,wantToSee,graphName)

#Implimentation w/ Argpars(not working on my computer bc of issue with my virtual env modules not importing right, may work on yours
#parser = argparse.ArgumentParser()
#parser.add_argument("height", help="height of each frame",type=int)
#parser.add_argument("width", help="width of each frame",type=int)
#parser.add_argument("binFilePath", help="path to the.bin file with annotation map data",type=int)
#try:#type=str bc user wants to plot a histogram for "all"
    #parser.add_argument("wantToSee", help="Histogram will be shown for this data. Either enter a frame number or "all" to see a histogram for the entire video",type=str)
#except:#type=int bc user wants to plot a histogram for a frame number
    #parser.add_argument("wantToSee", help="Histogram will be shown for this data. Either enter a frame number or "all" to see a histogram for the entire video",type=int)
#parser.add_argument("graphName", help="path to the image file of the matplotlib histogram. Make Sure to include the ending format(i.e. write "graph.png" not just "graph" for this argument),type=str)
#args = parser.parse_args()
#main(args.height,args.width,args.binFilePath,args.wantToSee,args.graphName)



