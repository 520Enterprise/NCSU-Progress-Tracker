def sum_lists(lists):
    total = 0
    for i in lists:
        product = 1
        for n in i:
            product *= n
        total += product
    return total
