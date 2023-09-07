def count_character(filename,character):
    count = 0
    with open(filename,'r') as fin:
        for line in fin:
            for character01 in line:
                if character01 == character:
                    count += 1
    return count
