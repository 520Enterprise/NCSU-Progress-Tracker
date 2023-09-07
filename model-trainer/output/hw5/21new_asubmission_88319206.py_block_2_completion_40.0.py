def hailstone(start): 
    count = 0
    while start != 1:
        if int(start % 2) == 0:
            print(start, end = ',')
            start /= 2
