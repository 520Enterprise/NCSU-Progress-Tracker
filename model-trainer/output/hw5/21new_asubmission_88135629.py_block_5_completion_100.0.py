def hailstone(start):
    integer = 1
    print(start, end = ',')
    while start != 1:
        if start % 2 == 0:
            start = start // 2
        else:
            start = start * 3 + 1
        print(start, end = ',')
        integer = integer + 1
    return integer
def main():
    user_input = int(input("Enter a number: "))
    print(hailstone(user_input))
if __name__ == '__main__':
    main()
