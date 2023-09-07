def sum_lists(lists):
#@#
    sumtotal = 0
    for single in lists:
#@#
        singletotal = 1
        for number in single:
            singletotal *= number
        sumtotal += singletotal
#@#
    return sumtotal
#@#
def main():
    test = sum_lists([[0,7,9,-4],[13,21,9,-2]])
    print(test)
if __name__ == '__main__':
    main()
#@#