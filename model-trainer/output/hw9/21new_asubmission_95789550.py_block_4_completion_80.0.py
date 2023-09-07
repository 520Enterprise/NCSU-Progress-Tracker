def input_tracker(number):
    recordings = {}
    record=0
    for ask in range(number):
        record = input("Enter Value "+ str(ask+1)+": ")
        if record in recordings: 
            recordings[record]+=1
        else: recordings[record]=1
    return recordings       
