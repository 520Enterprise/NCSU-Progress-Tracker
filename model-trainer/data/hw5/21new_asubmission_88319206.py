def hailstone(start): 
    count = 0
    while start != 1:
#@#
        if int(start % 2) == 0:
            print(start, end = ',')
            start /= 2
#@#
            start = int(start)
            count += 1
        else:
            print(start, end = ',')
            start = (start * 3) + 1
#@#
            count += 1
    print(start)  
    return count + 1
#@#
def test_hailstone():
    print("Testing hailstone(3))")
    print("3,10,5,16,8,4,2,1")
    expected = 8
    actual = hailstone(3)
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
    print("Testing hailstone(18))")
    print("18,9,28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1")
    expected = 21
    actual = hailstone(18)
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
    print("Testing hailstone(8))")
    print("8,4,2,1")
    expected = 4
    actual = hailstone(8)
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
def main():
    test_hailstone()
if __name__ == '__main__':
    main()
#@#