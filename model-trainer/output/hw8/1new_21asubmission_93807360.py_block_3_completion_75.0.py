def sum_lists(lists):
    total = 0 
    result = []
    for arguments in lists: 
        mult = 1
        for m in arguments: 
            mult = mult*m
        result.append(mult)
    for mult in result: 
        total += mult
