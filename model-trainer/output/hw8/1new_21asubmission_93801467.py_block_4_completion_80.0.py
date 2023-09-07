def sum_lists(lists):
    summ = 0
    for sublist in lists:
        i = 1
        for character in sublist:
            i = i * character
        summ = summ + i
    return summ
