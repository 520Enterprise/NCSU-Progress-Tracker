def count_character(filename, character):
    file = open(filename, "r")
    data = file.read()
    return data.count(character)
