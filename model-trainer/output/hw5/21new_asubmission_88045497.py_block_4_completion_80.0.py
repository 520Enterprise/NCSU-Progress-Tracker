def hailstone(start):
    if start > 0:
        num = start
        count = 1
        print (int(num), end = ',')
        while num != 1:
            if num % 2 == 0:
                num = num / 2
                count += 1
                print(int(num), end = ',')
            else:
                num = (num * 3) + 1
                count += 1
                print(int(num), end = ',')
        return (count)
    else:
        print('Please enter a positive integer.')
