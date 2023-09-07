def input_tracker(number):
    dictionary = {}
    for i in range(number):
        inp = input('Enter a value: ')
        if inp in dictionary:
            dictionary[inp] += 1
        else:
