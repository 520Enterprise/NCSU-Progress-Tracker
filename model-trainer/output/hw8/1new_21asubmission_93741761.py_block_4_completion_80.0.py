def sum_lists(lists):
    result = []
    for lis in lists:
        total = 1
        for x in lis:
            total *= x
        result.append(total)
    return sum(result)
