def count_character(filename,character):
    counter = 0
    with open(filename, 'r') as f:
        words = f.read()
        for c in words:
            if c == character:
                counter += 1
    return counter
