def input_tracker(number):
    i = 0
    inputs = {}
    while i != number:
        value = input("Enter a value:")
        if value in inputs:
            inputs[value] += 1
        else:
            inputs[value] = 1
        i += 1
    return inputs
def test_input_tracker():
    print("Testing input_tracker(4) with inputs 'A', 'C', 'B', 'A'")
    expected =  {'A': 2, 'B': 1, 'C': 1}
    actual = input_tracker(4)
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
    print("Testing input_tracker(6) with inputs '13', '45', '13', 'True', 'False', 'True'")
    expected =  {'13': 2, '45': 1, 'True': 2, 'False': 1}
    actual = input_tracker(6)
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
    print("Testing input_tracker(2) with inputs 'Yes', 'No'")
    expected =  {'Yes': 1, 'No': 1}
    actual = input_tracker(2)
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
def main():
    test_input_tracker() 
if __name__ == '__main__':
    main()
