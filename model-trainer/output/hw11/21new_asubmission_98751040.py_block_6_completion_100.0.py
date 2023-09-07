import numpy as np
def pair_max(arr1, arr2):
    maxxes = arr1.copy()
    for i in range(len(arr2)):
        if arr1[i] < arr2[i]:
            maxxes[i] = arr2[i]
    return maxxes
def main():
    arr5 = np.array([15, 18, 21, 24, 27, 30])
    arr6 = np.array([6, 12, 18, 24, 30, 36])
    print(pair_max(arr5, arr6))
    arr3 = np.array([0,0,0,0])
    arr4 = np.array([-1,1,-2,2])
    print(pair_max(arr3, arr4))
if __name__ == '__main__':
    main()
