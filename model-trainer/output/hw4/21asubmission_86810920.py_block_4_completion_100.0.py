def shipping_rate(lbs):
    if lbs <= 2:
        return lbs * 1.5
    elif lbs > 2 and lbs < 6:
        return (2*1.5)+(lbs-2)*3
    elif lbs > 6 and lbs < 10:
        return (2*1.5)+(4*3)+(lbs-6)*4
    else:
        return (2*1.5)+(4*3)+(4*4)+(lbs-10)*4.75
