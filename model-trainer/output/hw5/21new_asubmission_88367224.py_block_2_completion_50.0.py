def hailstone(start):
    int_count = 0                      
    while (start != 1):                
        print(int(start), end = ',')   
        if start % 2 == 0:             
            start = start / 2
