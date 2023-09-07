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
