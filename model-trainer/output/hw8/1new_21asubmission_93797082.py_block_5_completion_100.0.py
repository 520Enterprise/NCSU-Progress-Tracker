def sum_lists(lists):
    i = 0
    summ = 0
    while i < len(lists):
        fill = tuple(lists[i])
        x = 0
        num = 1
        while x < len(fill):
            num *= fill[x]
            x += 1
        summ += num
        i += 1
    return summ
def main():
if __name__ == '__main__':
    main()
