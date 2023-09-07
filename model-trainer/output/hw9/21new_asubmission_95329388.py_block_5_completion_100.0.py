def input_tracker(number):
    dictionary = {}
    for inpt in range(number):
        v = input('Enter a value: ')
        if v in dictionary: 
            dictionary[v] += 1 
        else:
            dictionary[v] = 1
    return dictionary
def main():
    print(input_tracker(4))
if __name__ == '__main__':
    main()
