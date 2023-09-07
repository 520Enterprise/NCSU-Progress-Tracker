def sum_lists(lists):
    total = 0
    for i in lists:
        product = 1
        n = 0
        while n < len(i):
            product *= i[n]
            n += 1
        total += product
    return total
def main():
if __name__ == '__main__':
    main()
