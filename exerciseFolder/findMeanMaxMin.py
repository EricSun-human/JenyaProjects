import numpy as np

arrayOne = np.random.rand(3,3)
arrayTwo = np.random.rand(3,3)
arrayThree = np.random.rand(3,3)

combinedArray = np.stack((arrayOne,arrayTwo,arrayThree),axis=2)
#print(combinedArray.ndim)
print(combinedArray)

def findMinMaxMeanEntireArray():
    minNum = round(np.min(combinedArray),3)
    maxNum = round(np.max(combinedArray),3)
    meanNum = round(np.mean(combinedArray),3)
    print("Minimum: "+str(minNum))
    print("Maximum: "+str(maxNum))
    print("Average: "+str(meanNum))

#findMinMaxMeanEntireArray()
def findMinMaxMeanArrayAxis():
    #arrayOne = np.array([[1,2,3],[1,2,3],[1,2,3]])
    #arrayTwo = np.array([[5,6,7],[5,6,7],[5,6,7]])
    #arrayThree = np.array([[8,9,10],[8,9,10],[8,9,10]])
    print("Max Vertical Value: "+str(np.amax(combinedArray, axis=0)))
    print("Max Horizontal Value: "+str(np.amax(combinedArray, axis=1)))
    print("Max Depth Value: "+str(np.amax(combinedArray, axis=2)))

findMinMaxMeanEntireArray()
findMinMaxMeanArrayAxis()
