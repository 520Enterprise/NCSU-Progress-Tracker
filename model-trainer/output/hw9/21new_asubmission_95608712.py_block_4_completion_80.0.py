def input_tracker(number):
    final = {}
    counter = 0
    while counter < number:
        uinput = input("Please enter an input: ")
        if uinput in final:
            final[uinput] += 1
        else:
            final[uinput] = 1
        counter += 1
    return final
