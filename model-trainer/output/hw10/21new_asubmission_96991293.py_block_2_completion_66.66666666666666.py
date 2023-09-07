def count_character(filename, character):
    count = 0
    with open(filename, 'r') as fi:
        for k in fi:
