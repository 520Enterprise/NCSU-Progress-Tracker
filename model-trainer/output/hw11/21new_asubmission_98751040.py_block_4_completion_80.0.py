import numpy as np
def pair_max(arr1, arr2):
    maxxes = arr1.copy()
    for i in range(len(arr2)):
        if arr1[i] < arr2[i]:
            maxxes[i] = arr2[i]
