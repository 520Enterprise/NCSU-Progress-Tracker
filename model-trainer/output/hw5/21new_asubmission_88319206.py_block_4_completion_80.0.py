def hailstone(start): 
    count = 0
    while start != 1:
        if int(start % 2) == 0:
            print(start, end = ',')
            start /= 2
            start = int(start)
            count += 1
        else:
            print(start, end = ',')
            start = (start * 3) + 1
            count += 1
    print(start)  
    return count + 1
