def count_character(filename, character):
    f = open(filename, 'r')
    text = f.read()
    return text.count(character)
