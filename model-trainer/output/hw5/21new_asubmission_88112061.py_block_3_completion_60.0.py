import math
def hailstone(start):
    number = start
    count = 1
    while start > 1:
        start = int(start)
        print(start, end = ',')
        if start % 2 == 0:
            start = start / 2
        else:
            start = start * 3 + 1
