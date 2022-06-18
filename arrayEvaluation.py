import numpy as np

arrayOne = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
arrayTwo = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
arrayThree = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
print(arrayOne.shape)
print(arrayOne.ndim)
#combinedArray = np.concatenate(arrayOne,arrayTwo)
combinedArray = np.append(arrayOne,arrayTwo)
combinedArray = np.append(combinedArray,arrayThree)
print(combinedArray)
combinedArray = np.reshape(combinedArray,(3,6,3))
print(combinedArray)
print(combinedArray.ndim)