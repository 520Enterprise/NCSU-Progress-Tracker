def shipping_rate(lbs):
    if lbs <= 2:
        return lbs * 1.5
    elif lbs > 2 and lbs < 6:
        return (2*1.5)+(lbs-2)*3
