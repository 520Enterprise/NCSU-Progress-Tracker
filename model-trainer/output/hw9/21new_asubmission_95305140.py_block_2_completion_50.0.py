def input_tracker(number):
    d = {}
    for i in range(number):
        user = input('Enter an value: ')
        if user in d:
