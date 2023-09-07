import numpy as np
def pair_max(arr1,arr2):
    for i in range(len(arr1)):
        if arr1[i]<arr2[i]:
            arr1[i] = arr2[i]
    return arr1
