import numpy as np
#@#
def pair_max(arr1, arr2):
#@#
    maxm = np.zeros(np.size(arr1))
    for i in range(np.size(arr1)):
#@#
        if arr1[i]>=arr2[i]:
            maxm[i] = arr1[i]
        else:
            maxm[i] = arr2[i]
#@#
    return(maxm)
#@#
def main():
    print(pair_max(np.array([1,9,2,8,3]),np.array([0,5,14,5,6])))
if __name__ == '__main__':
    main()
#@#