def count_character(filename, character):
    f = open(filename, 'r')
    res = 0
    for i in f.read():
        if i == character:
            res = res + 1
    return res
