import numpy as np
def pair_max(arr1, arr2):
    array = []
    for i,j in zip(arr1, arr2):
        array.append(max(i,j))
    pairwise_max = np.array(array)
    return pairwise_max
arr1 = np.array([1,9,2,8,3])
arr2 = np.array([0,5,14,5,6])   
arr3 = np.array([0,0,0,0])
arr4 = np.array([-1,1,-2,2])
arr5 = np.array([15, 18, 21, 24, 27, 30])
arr6 = np.array([6, 12, 18, 24, 30, 36])
def main():
    print(pair_max(arr1, arr2))
    print(pair_max(arr3, arr4))
    print(pair_max(arr5, arr6))
if __name__ == '__main__':
    main()
