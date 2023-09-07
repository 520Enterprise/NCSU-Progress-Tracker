import numpy as np
#@#
def pair_max(arr1,arr2):
#@#
    for i in range(len(arr1)):
#@#
        if arr1[i]<arr2[i]:
            arr1[i] = arr2[i]
#@#
    return arr1
#@#
def main():
    arr3 = pair_max([1,9,2,8,3],[0,5,14,5,6])
    print(arr3)
if __name__ == '__main__':
    main()
#@#