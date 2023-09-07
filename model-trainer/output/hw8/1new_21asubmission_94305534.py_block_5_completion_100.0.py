def sum_lists(lists):
    total = 0
    for sublist in lists:
        product = 1
        for item in sublist:
            product *= item
        total += product
    return round(total, 10) 
def main():
    print(sum_lists([[1,2],[3,4],[5,6]]))
if __name__ == '__main__':
    main()
