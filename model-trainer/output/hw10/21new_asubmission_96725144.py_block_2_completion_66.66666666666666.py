def count_character(filename,character):
    count = 0 
    file = open(filename,'r')
    words = file.read()
    for letters in words: 
