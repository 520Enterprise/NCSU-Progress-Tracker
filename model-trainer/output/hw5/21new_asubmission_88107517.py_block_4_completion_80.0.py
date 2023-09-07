def hailstone(start):
    num = 0
    num += 1
    while start != 1:
        num += 1
        print(int(start), end = ',')
        if start % 2 == 0:
            start = start / 2 
        elif start % 2 != 0:
            start = start * 3 + 1
    else:
        start == 1
        print(int(start))
    return num 
