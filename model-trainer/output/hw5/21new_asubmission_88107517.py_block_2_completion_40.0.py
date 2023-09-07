def hailstone(start):
    num = 0
    num += 1
    while start != 1:
        num += 1
        print(int(start), end = ',')
        if start % 2 == 0:
            start = start / 2 
