def sum_lists(lists):
#@#
    result = []
    for lis in lists:
#@#
        total = 1
        for x in lis:
            total *= x
        result.append(total)
#@#
    return sum(result)
#@#
def main():
    print(sum_lists([[1, 2], [3, 4],[5,6]]))
    print(sum_lists([[3, 0.1], [0.04,.001]]))
    print(sum_lists([[0,7,9,-4], [13,21,9,-2]]))
if __name__ == '__main__':
    main()
#@#