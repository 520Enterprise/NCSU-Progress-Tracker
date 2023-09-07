def sum_lists(lists):
    total = 0                                    
    for i in range(len(lists)):                  
        product = 1                              
        for j in range(len(lists[i])):           
            product *= lists[i][j]               
        total += product                         
    return total                                 
def testing_sum_lists():
    print()
    print("Testing sum_lists([[1,2],[3,4],[5,6]])")
    expected = 44
    actual = sum_lists([[1,2],[3,4],[5,6]])
    if expected == actual:
        print("Test passed!")
        print("Expected: ", expected)
        print("Actual: ", actual)
    else:
        print("Test failed.")
        print("Expected: ", expected)
        print("Actual: ", actual)
    print()
    print("Testing sum_lists([[3,0.1],[0.04,0.001])")
    expected = 0.30004
    actual = sum_lists([[3,0.1],[0.04,0.001]])
    if (actual - 0.00001) <= actual <= (actual + 0.00001):     
        print("Test passed!")
        print("Expected: ", expected)
        print("Actual: ", actual)
    else:
        print("Test failed.")
        print("Expected: ", expected)
        print("Actual: ", actual)
    print()
    print("Testing sum_lists([[0,7,9,-4],[13,21,9,-2]])")
    expected = -4914
    actual = sum_lists([[0,7,9,-4],[13,21,9,-2]])
    if expected == actual:
        print("Test passed!")
        print("Expected: ", expected)
        print("Actual: ", actual)
    else:
        print("Test failed.")
        print("Expected: ", expected)
        print("Actual: ", actual)
def main():
    testing_sum_lists()
if __name__ == '__main__':
    main()
