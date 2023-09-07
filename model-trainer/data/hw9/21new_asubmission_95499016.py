def input_tracker(number):
    d = {} 
    l = []
    value = 0
    for iterations in range(number): 
#@#
        keys = input('Please input a value: ')
        l.append(keys)
        d[keys] = value
    for k in l: 
        for key in d:
            if key == k:
                d[k] += 1
    return d 
#@#
def main():
if __name__ == '__main__':
    main()
#@#