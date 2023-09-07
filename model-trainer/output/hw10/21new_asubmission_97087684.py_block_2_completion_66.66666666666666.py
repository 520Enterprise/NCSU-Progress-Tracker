def count_character(filename, character):
    with open(filename,'r') as file:
        count = 0
        line = file.read()
        for cha in list(line):
