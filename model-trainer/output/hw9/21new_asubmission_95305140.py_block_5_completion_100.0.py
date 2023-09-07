def input_tracker(number):
    d = {}
    for i in range(number):
        user = input('Enter an value: ')
        if user in d:
            d[user]+=1
        else:
            d[user]=1
    return d
def main():
    print(input_tracker(2))
if __name__ == '__main__':
    main()
