import numpy as np
#@#
def pair_max(arr1, arr2):
#@#
    lst = []
    count = 0
    for item in arr1:
#@#
        if item > arr2[count]:
            lst.append(item)
        elif arr2[count] >= item:
            lst.append(arr2[count])
#@#
        count += 1
    return np.array(lst)
#@#
def main():
if __name__ == '__main__':
    main()
#@#