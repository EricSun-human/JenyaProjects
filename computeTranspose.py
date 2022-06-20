import numpy as np

originalArray = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(originalArray.ndim)
print(originalArray.shape)
print(originalArray)
flippedArray=originalArray.transpose()
print(flippedArray)
