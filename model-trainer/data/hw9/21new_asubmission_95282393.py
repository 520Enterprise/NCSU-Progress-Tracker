def input_tracker(number):
    dict01 = {}
    for n in range(number):
#@#
        a = input("Enter an input: ")
        if a not in dict01.keys():
#@#
            dict01[a] = 1
        elif a in dict01.keys():
#@#
            dict01[a] += 1 
    return dict01
#@#
def main():
    print(input_tracker(2))
if __name__ == '__main__':
    main()
#@#