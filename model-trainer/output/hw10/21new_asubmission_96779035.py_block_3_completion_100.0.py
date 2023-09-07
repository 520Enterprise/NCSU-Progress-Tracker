def count_character(filename, character):
    file = open(filename, 'r')
    book = file.read()
    return book.count(character)
