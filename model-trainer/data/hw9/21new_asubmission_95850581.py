def input_tracker(number):
    dictionary = {}
    for i in range(number):
#@#
        inp = input('Enter a value: ')
        if inp in dictionary:
#@#
            dictionary[inp] += 1
        else:
#@#
            dictionary[inp] = 1
    return dictionary
#@#
def main():
if __name__ == '__main__':
    main()
#@#