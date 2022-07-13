import numpy as np

def get_data_from_annotation_array(height, width, annotation_buffer):
    '''returns array with dims: height, width, numFrames'''
    print("annotation_buffer type: "+str(type(annotation_buffer)))
    #print("annotation_buffer len: "+str(len(annotation_buffer)))
    print("annotation_buffer type"+str(type(annotation_buffer)))
    annotation = np.frombuffer(annotation_buffer, dtype=np.uint8) # Get error on this line-->TypeError: memoryview: a bytes-like object is required, not '_io.BufferedReader'
    annotation_np = annotation.reshape(width, height, -1, order='F').swapaxes(0, 1)
    return annotation_np.astype('float32')

output_file = open("C:\\Users\\erics\\Downloads\\jenya_4b3962e8-faba-4535-9c35-b3df955f2c9e_5_x264.bin", 'rb')
print("output_file data:"+str(output_file))
#for line in output_file:
    #print("\n"+str(line))

videoArray = get_data_from_annotation_array(270, 480,output_file)
print(videoArray.shape)
