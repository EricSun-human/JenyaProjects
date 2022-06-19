import numpy as np

arrayOne = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
arrayTwo = np.array([[5,6,7,8,9],[5,6,7,8,9],[5,6,7,8,9],[5,6,7,8,9],[5,6,7,8,9],[5,6,7,8,9]])
#arrayThree = np.array([[1,1,1,1,1][2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]])

arrayOne = np.arange(0,5*6,1).reshape((5,6))
arrayTwo = np.arange(0,5*6,1).reshape((5,6))+30
arrayThree = np.arange(0,5*6,1).reshape((5,6))+60

print(arrayOne.shape)
print(arrayOne.ndim)
combinedArray = np.stack((arrayOne,arrayTwo,arrayThree),axis=2)
#combinedArray = np.append(arrayOne,arrayTwo)
#combinedArray = np.append(combinedArray,arrayThree)
print(combinedArray)
#combinedArray = np.reshape(combinedArray,(3,6,3))
#print(combinedArray)
print(combinedArray.shape)
