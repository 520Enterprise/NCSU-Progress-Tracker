def sum_lists(lists):
    total = 0                                    
    for i in range(len(lists)):                  
        product = 1                              
        for j in range(len(lists[i])):           
            product *= lists[i][j]               
        total += product                         
