def alphabetical(sentence):
    ordered_list = sentence.split()
    ordered_list.sort()
    return ordered_list
def testing_alphabetical():
    print("Testing alphabetical('Welcome to CSC111!')")
    expected = ['CSC111!', 'Welcome', 'to']
    actual = alphabetical("Welcome to CSC111!")
    if expected == actual:
        print ("Test passed!")
    else:
        print("Test Failed")
        print("Expected:",expected)
        print("Actual:",actual)
    print("Testing alphabetical('Do your homework')")
    expected = ['Do', 'homework', 'your']
    actual = alphabetical("Do your homework")
    if expected == actual:
        print ("Test passed!")
    else:
        print("Test Failed")
        print("Expected:",expected)
        print("Actual:",actual)    
def main():
    testing_alphabetical()
if __name__ == '__main__':
    main()
