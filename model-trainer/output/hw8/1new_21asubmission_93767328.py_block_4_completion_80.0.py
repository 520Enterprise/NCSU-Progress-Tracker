def sum_lists(lists):
    sum01 = 0
    for list01 in lists:
        total = 1
        for values in list01:
            total = total * values
        sum01 += total
    return sum01
