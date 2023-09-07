def hailstone(start):
    if start == 1:
        print("1")
        return 1
    elif start > 1:
        loops = 0
        while start != 1:
            loops += 1
            print(start , end = ',')
            if start % 2 == 0:
                start = start/2
                start = int(start)
            else:
                start = (start*3) + 1
                start = int(start)
        print("1")
        loops += 1
        return loops
def main():
    hailstone(8)
if __name__ == '__main__':
    main()
