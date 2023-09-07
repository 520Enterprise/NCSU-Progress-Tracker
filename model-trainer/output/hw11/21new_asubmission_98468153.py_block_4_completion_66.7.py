import numpy as np
def pair_max(arr1, arr2):
    pair_max = np.array([])
    for i in range(np.size(arr1)):
        if arr1[i] > arr2[i]:
            largest = arr1[i]
            pair_max = np.append(pair_max, largest)
        else: 
            largest = arr2[i]
            pair_max = np.append(pair_max, largest)  
