def sum_lists(lists):
    i = 0
    summ = 0
    while i < len(lists):
        fill = tuple(lists[i])
        x = 0
        num = 1
        while x < len(fill):
            num *= fill[x]
            x += 1
        summ += num
