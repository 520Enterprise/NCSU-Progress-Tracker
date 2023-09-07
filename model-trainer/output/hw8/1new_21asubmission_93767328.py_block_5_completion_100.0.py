def sum_lists(lists):
    sum01 = 0
    for list01 in lists:
        total = 1
        for values in list01:
            total = total * values
        sum01 += total
    return sum01
def main():
    print(sum_lists([[1,2],[3,4],[5,6]]))
    print(sum_lists([[3,0.1],[0.04, 0.001]]))
    print(sum_lists([[0,7,9,-4], [13,21,9,-2]]))
if __name__ == '__main__':
    main()
