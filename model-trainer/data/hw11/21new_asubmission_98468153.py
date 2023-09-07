import numpy as np
#@#
def pair_max(arr1, arr2):
#@#
    pair_max = np.array([])
    for i in range(np.size(arr1)):
#@#
        if arr1[i] > arr2[i]:
            largest = arr1[i]
            pair_max = np.append(pair_max, largest)
        else: 
            largest = arr2[i]
            pair_max = np.append(pair_max, largest)  
#@#
        i += 1
    return pair_max
#@#
def testing_pair_max():
    arr1 = np.array([1,9,2,8,3])
    arr2 = np.array([0,5,14,5,6])
    print("Testing pair_max(arr1, arr2)")
    expected = np.array([1, 9, 14, 8, 6 ])
    actual = pair_max(arr1, arr2)
    if np.array_equal(expected, actual):
        print("Test Passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
    arr3 = np.array([0,0,0,0])
    arr4 = np.array([-1,1,-2,2])
    print("Testing pair_max(arr3, arr4)")
    expected = np.array([0, 1, 0, 2])
    actual = pair_max(arr3, arr4)
    if np.array_equal(expected, actual):
        print("Test Passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
    arr5 = np.array([15,18,21,24,27,30])
    arr6 = np.array([6,12,18,24,30,36])
    print("Testing pair_max(arr5, arr6)")
    expected = np.array([15, 18, 21, 24, 30, 36])
    actual = pair_max(arr5, arr6)
    if np.array_equal(expected, actual):
        print("Test Passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
def main():
    testing_pair_max()
if __name__ == '__main__':
    main()
#@#