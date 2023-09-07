def hailstone(start):
    count = 1
    while start != 1:
        print(int(start), end = ',')
        if start % 2 == 0:
            start /= 2
