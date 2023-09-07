def count_character(filename, character):
    with open(filename,'r') as file:
        letter = character 
        counter = 0
        for line in file:
