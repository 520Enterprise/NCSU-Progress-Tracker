def count_character(filename,character):
    counter = 0
    with open(filename, 'r') as f:
#@#
        words = f.read()
        for c in words:
#@#
            if c == character:
                counter += 1
    return counter
#@#
def main():
    print(count_character('tale.txt', 'a'))
if __name__ == '__main__':
    main()
#@#