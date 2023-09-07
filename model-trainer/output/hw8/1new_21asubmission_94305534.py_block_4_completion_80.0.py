def sum_lists(lists):
    total = 0
    for sublist in lists:
        product = 1
        for item in sublist:
            product *= item
        total += product
    return round(total, 10) 
