def input_tracker(number):
    dictionary = {}
    for inpt in range(number):
        v = input('Enter a value: ')
        if v in dictionary: 
            dictionary[v] += 1 
        else:
            dictionary[v] = 1
    return dictionary
