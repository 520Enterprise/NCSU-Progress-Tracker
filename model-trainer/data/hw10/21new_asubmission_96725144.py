def count_character(filename,character):
    count = 0 
    file = open(filename,'r')
#@#
    words = file.read()
    for letters in words: 
#@#
        if letters == character:
            count += 1
    return count
#@#
def main():
if __name__ == '__main__':
    main()
#@#