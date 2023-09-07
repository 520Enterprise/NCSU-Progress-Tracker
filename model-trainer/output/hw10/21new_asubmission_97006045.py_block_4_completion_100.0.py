def count_character(filename, character):
    f = open(filename, 'r')
    res = 0
    for i in f.read():
        if i == character:
            res = res + 1
    return res
def main():
    print(count_character('hello.txt', 'L'))
    print(count_character('hello.txt', 'H'))
    print(count_character('hello.txt', 'e'))
if __name__ == '__main__':
    main()
