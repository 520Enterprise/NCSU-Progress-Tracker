def alphabetical(sentence):
    sentence = sentence.split(" ")
    sentence.sort()
    return sentence
def testing_alphabetical():
    print("Testing alphabetical(Down we dive)")
    expected = ['Down', 'dive', 'we']
    actual = alphabetical("Down we dive")
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
    print("Testing alphabetical(Apples with oranges!)")
    expected = ['Apples', 'oranges!', 'with']
    actual = alphabetical("Apples with oranges!")
    if expected == actual:
        print("Test passed!")
    else:
        print("Test failed.")
        print("Expected:", expected)
        print("Actual:", actual)
def main():
    testing_alphabetical()
if __name__ == '__main__':
    main()
