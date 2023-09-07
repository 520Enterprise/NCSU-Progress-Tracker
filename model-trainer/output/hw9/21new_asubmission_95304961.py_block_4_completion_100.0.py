def input_tracker(number):
    dicot = {}
    for i in range(number):
        j = input('Please enter an Answer: ')
        if j in dicot:
            dicot[j] += 1
        else:
            dicot[j] = 1
    return dicot
