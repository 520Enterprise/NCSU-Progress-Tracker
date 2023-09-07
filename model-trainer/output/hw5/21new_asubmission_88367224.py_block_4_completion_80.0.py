def hailstone(start):
    int_count = 0                      
    while (start != 1):                
        print(int(start), end = ',')   
        if start % 2 == 0:             
            start = start / 2
        else:                          
            start = (start * 3) + 1    
        int_count += 1                 
    if start == 1:                     
        print(int(start))              
        int_count += 1                 
    return int_count                   
