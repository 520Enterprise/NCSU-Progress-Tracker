def hailstone(start):
    count = 1
    while start != 1:
#@#
        print(int(start), end = ',')
        if start % 2 == 0:
            start /= 2
#@#
        else:
            start = (start * 3) + 1
        count += 1
#@#
    print(int(start))
    return count
#@#
def main():
if __name__ == '__main__':
    main()
#@#