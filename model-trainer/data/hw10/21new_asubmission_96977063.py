def count_character(filename, character):
    with open(filename,'r') as file:
#@#
        letter = character 
        counter = 0
        for line in file:
#@#
            for character in line:
                if letter == character:
                    counter += 1
        return counter
#@#
def test_count_character():
    print("Testing count_character('hello.txt', 'L')")
    expected =  4
    actual = count_character('hello.txt', 'L')
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
    print("Testing count_character('hello.txt', 'H')")
    expected =  4
    actual = count_character('hello.txt', 'H')
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
    print("Testing count_character('hello.txt', 'e')")
    expected =  2
    actual = count_character('hello.txt', 'e') 
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
def main():
    test_count_character()
if __name__ == '__main__':
    main()
#@#