def sum_lists(lists):
    sumtotal = 0
    for single in lists:
        singletotal = 1
        for number in single:
            singletotal *= number
        sumtotal += singletotal
