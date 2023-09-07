def count_character(filename, character):
    count = 0
    with open(filename, 'r') as fi:
#@#
        for k in fi:
#@#
            for i in k:
                if i == character:
                    count += 1
                else:
                    continue
    return count
#@#
def main():
if __name__ == '__main__':
    main()
#@#