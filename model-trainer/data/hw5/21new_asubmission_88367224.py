def hailstone(start):
    int_count = 0                      
    while (start != 1):                
#@#
        print(int(start), end = ',')   
        if start % 2 == 0:             
            start = start / 2
#@#
        else:                          
            start = (start * 3) + 1    
#@#
        int_count += 1                 
    if start == 1:                     
        print(int(start))              
        int_count += 1                 
    return int_count                   
#@#
def testing_hailstone():
    print("Testing hailstone(3)")
    expected = 8
    actual = hailstone(3)
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected: ", expected)
        print("Actual: ", actual)
    print("Testing hailstone(18)")
    expected = 21
    actual = hailstone(18)
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected: ", expected)
        print("Actual: ", actual)
    print("Testing hailstone(8)")
    expected = 4
    actual = hailstone(8)
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected: ", expected)
        print("Actual: ", actual)
def main():
    testing_hailstone()
if __name__ == '__main__':
    main()
#@#