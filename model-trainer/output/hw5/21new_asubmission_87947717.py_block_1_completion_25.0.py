def hailstone(start):
    if start == 1:
        print("1")
        return 1
    elif start > 1:
        loops = 0
        while start != 1:
