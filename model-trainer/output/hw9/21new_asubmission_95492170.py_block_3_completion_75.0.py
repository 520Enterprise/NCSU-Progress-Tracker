def input_tracker(number):
    i = 0
    inputs = {}
    while i != number:
        value = input("Enter a value:")
        if value in inputs:
            inputs[value] += 1
        else:
